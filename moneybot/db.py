from moneybot import config
from moneybot.exc import NoSuchQuery
from os import listdir
from os.path import exists, join
from sqlite3 import connect


DB = {
    'conn': None
}


def get_con():
    return DB['conn']


def get_query_contents(name):
    return open(join(config.SQL_PATH, name)).read().replace("\n", " ").strip()


def insert(query_name, *args, **kwargs):
    query = QUERIES.get(query_name)

    if query is None:
        raise NoSuchQuery(query_name)


def select(query_name, *args, **kwargs):
    pass


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


QUERIES = {
    i.replace('sql', ''): get_query_contents(i)
    for i in listdir(config.SQL_PATH)
    if i != config.SCHEMA_FILE_NAME
}
