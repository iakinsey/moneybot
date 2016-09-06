from moneybot import config
from moneybot.exc import NoSuchQuery
from os import listdir
from os.path import exists, join
from sqlite3 import connect, Error as SqliteError


def get_con():
    return DB['conn']


def get_query_contents(name):
    return open(join(config.SQL_PATH, name)).read().replace("\n", " ").strip()


def get_query(query_name):
    query = QUERIES.get(query_name)

    if query is None:
        raise NoSuchQuery(query_name)

    return query


async def insert(query_name, *args, **kwargs):
    # TODO something smarter
    await execute(query_name, *args)


async def select(query_name, *args, **kwargs):
    # If set to true, then only send the first result.
    first = kwargs.get("first", False)
    con, cur = await execute(query_name, *args)

    if first:
        return cur.fetchone()
    else:
        return cur.fetchall()


async def execute(query_name, *args):
    query = get_query(query_name)
    con = get_con()
    cur = con.cursor()

    try:
        cur.execute(query, args)
    except SqliteError:
        con.rollback()
        raise
    else:
        con.commit()

    return con, cur


def setup_database():
    database_exists = exists(config.DB_PATH)
    DB['conn'] = connect(config.DB_PATH)
    con = get_con()

    if database_exists:
        return

    # Create schema
    with open(config.SCHEMA_FILE_PATH, 'r') as f:
        queries = [i for i in f.read().split(";") if i]

    with con:
        for query in queries:
            con.execute(query)


DB = {
    'conn': None
}


QUERIES = {
    i.replace('.sql', ''): get_query_contents(i)
    for i in listdir(config.SQL_PATH)
    if i != config.SCHEMA_FILE_NAME
}
