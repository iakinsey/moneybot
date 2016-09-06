from moneybot import config
from moneybot.db import setup_database
from moneybot.app import connect_to_discord
from moneybot.command import setup_commands
from os import mkdir
from os.path import exists

def setup_data_path():
    if not exists(config.DATA_PATH):
        mkdir(config.DATA_PATH)

def start_bot():
    setup_data_path()
    setup_database()
    setup_commands()
    connect_to_discord()


if __name__ == "__main__":
    start_bot()
