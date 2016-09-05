from os.path import dirname, realpath, join, abspath


PROJECT_ROOT = abspath(dirname(dirname(realpath(__file__))))
DATA_PATH = join(PROJECT_ROOT, 'data')
DB_PATH = join(DATA_PATH, 'ledger.db')
SQL_PATH = join(PROJECT_ROOT, 'sql')
SCHEMA_FILE_NAME = 'schema.sql'
SCHEMA_FILE_PATH = join(SQL_PATH, SCHEMA_FILE_NAME)
DISCORD_TOKEN = ""
