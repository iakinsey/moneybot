from moneybot.db import insert, select


def update_balance(channel_id, user_id, amount):
    insert('update_balance', channel_id, user_id, amount)


def transfer_balance(channel_id, source_user_id, destination_user_id, amount):
    balance = select('get_user_balance', channel_id, source_user_id)

    if not balance:
        pass


def get_user_balance(channel_id, user_id):
    pass


def get_channel_balances(channel_id):
    pass
