from os import environ
from os.path import dirname, realpath, join, abspath


def required(key):
    val = environ.get(key)

    if not val:
        print("Missing environment variable: '{}'".format(key))
        exit(1)

    return val


PROJECT_ROOT = abspath(dirname(dirname(realpath(__file__))))
COMMANDS_PATH = join(PROJECT_ROOT, 'moneybot', 'commands')
DATA_PATH = join(PROJECT_ROOT, 'data')
DB_PATH = join(DATA_PATH, 'ledger.db')
SQL_PATH = join(PROJECT_ROOT, 'sql')
SCHEMA_FILE_NAME = 'schema.sql'
SCHEMA_FILE_PATH = join(SQL_PATH, SCHEMA_FILE_NAME)
DISCORD_TOKEN = required("MONEYBOT_APP_KEY")
STEAL_FAILURE_PROBABILITY = .5
