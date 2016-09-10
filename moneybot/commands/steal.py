from moneybot import config
from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import get_user_balance, burn_balance, transfer_balance
from moneybot.util import format_int
from random import uniform, randrange


class Steal(Command):
    prefix = "steal"
    description = (
        "Steal a a random amount of money between 1 and the amount from a user "
        "with a {}% chance of losing that money. "
        "You can't steal more money than you currently have."
    ).format(int(config.STEAL_FAILURE_PROBABILITY * 100))
    examples = [
        "$steal @Moneybot 100",
        "$steal @user 9001"
    ]

    async def default(self):
        server_id = int(self.message.server.id)
        source_user_id = int(self.message.author.id)

        if len(self.tokens) != 3:
            raise InvalidCommand("Pay command was not formatted properly!")

        amount = self.parse_int(self.tokens[2])

        if amount is None:
            raise InvalidCommand("Amount must be an number!")

        if amount == 0:
            raise InvalidCommand("Do you even know how to steal?")

        if amount < 0:
            raise InvalidCommand("Amount can't be negative!")

        destination_user_id = self.parse_user_string(self.tokens[1])

        if not destination_user_id:
            raise InvalidCommand("No such user!")

        source_balance = await get_user_balance(server_id, source_user_id)
        destination_balance = await get_user_balance(server_id, destination_user_id)

        if source_balance < amount:
            msg = "You're too poor to steal that much money, go buy more money."
            raise InvalidCommand(msg)
        elif destination_balance < amount:
            msg = "<@{}> doesn't have that much money"
            raise InvalidCommand(msg.format(destination_user_id))

        probability = uniform(0, 1)
        steal_amount = randrange(int(amount / 2), amount) or 1
        response = "You lost {} of your own money in the heist, good job.".format(format_int(steal_amount))

        if probability > config.STEAL_FAILURE_PROBABILITY:
            # Success
            response = "Successfully stole {} from <@{}>.".format(format_int(steal_amount), destination_user_id)
            await transfer_balance(server_id, destination_user_id, source_user_id, steal_amount)
        else:
            # Failure
            await burn_balance(server_id, source_user_id, steal_amount)

        return response
