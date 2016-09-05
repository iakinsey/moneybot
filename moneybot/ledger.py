from moneybot.db import insert, select
from moneybot.exc import InsufficientFunds


def update_balance(channel_id, user_id, amount):
    insert('update_balance', channel_id, user_id, amount)


def transfer_balance(channel_id, source_user_id, destination_user_id, amount):
    balance = select('get_user_balance', channel_id, source_user_id, first=True)

    if not balance or amount > balance:
        msg = "You have insufficient funds! Current balance is: {}"
        raise InsufficientFunds(msg.format(balance))

    # TODO turn into a single transaction.
    insert('update_balance', channel_id, source_user_id, -amount)
    insert('update_balance', channel_id, destination_user_id, amount)


def get_user_balance(channel_id, user_id):
    return select('get_user_balance', channel_id, user_id, first=True) or 0


def get_channel_balances(channel_id):
    return select('get_channel_balances', channel_id)
