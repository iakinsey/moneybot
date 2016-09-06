from moneybot.db import insert, select
from moneybot.exc import InsufficientFunds


async def update_balance(server_id, user_id, amount):
    await insert('update_balance', server_id, user_id, amount)


async def transfer_balance(server_id, source_user_id, destination_user_id, amount):
    if amount < 0:
        raise InsufficientFunds("Can't send negative money!")

    balance = await get_user_balance(server_id, source_user_id)

    if not balance or amount > balance:
        msg = "You have insufficient funds! Current balance is: {}"
        raise InsufficientFunds(msg.format(balance))

    # TODO turn into a single transaction.
    await insert('update_balance', server_id, source_user_id, -amount)
    await insert('update_balance', server_id, destination_user_id, amount)


async def burn_balance(server_id, user_id, amount):
    balance = await get_user_balance(server_id, user_id)

    if not balance or amount > balance:
        msg = "You have insufficient funds! Current balance is: {}"
        raise InsufficientFunds(msg.format(balance))

    await insert('update_balance', server_id, user_id, -amount)


async def get_user_balance(server_id, user_id):
    result = await select('get_user_balance', server_id, user_id, first=True)

    if result:
        return result[0] or 0

    return 0


async def get_leaderboard(server_id):
    result = await select('get_leaderboard', server_id)

    return result


async def get_channel_balances(server_id):
    return await select('get_channel_balances', server_id)
