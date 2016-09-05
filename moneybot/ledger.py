from moneybot.db import insert, select
from moneybot.exc import InsufficientFunds


def update_balance(server_id, user_id, amount):
    insert('update_balance', server_id, user_id, amount)


def transfer_balance(server_id, source_user_id, destination_user_id, amount):
    if amount < 0:
        raise InsufficientFunds("Can't send negative money!")

    balance = get_user_balance(server_id, source_user_id)

    if not balance or amount > balance:
        msg = "You have insufficient funds! Current balance is: {}"
        raise InsufficientFunds(msg.format(balance))

    # TODO turn into a single transaction.
    insert('update_balance', server_id, source_user_id, -amount)
    insert('update_balance', server_id, destination_user_id, amount)


def get_user_balance(server_id, user_id):
    result = select('get_user_balance', server_id, user_id, first=True)

    if result:
        return result[0] or 0

    return 0


def get_channel_balances(server_id):
    return select('get_channel_balances', server_id)
