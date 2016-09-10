from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import burn_balance
from moneybot.util import format_int


class Burn(Command):
    prefix = "burn"
    description = "Burn money."
    examples = [
        "$burn",
        "$burn 1000000000"
    ]

    async def default(self):
        server_id = int(self.message.server.id)
        user_id = int(self.message.author.id)

        if len(self.tokens) != 2:
            raise InvalidCommand("Burn command was not formatted properly!")

        amount = self.parse_int(self.tokens[1])

        if amount is None:
            raise InvalidCommand("Amount must be an number!")

        if amount == 0:
            raise InvalidCommand("Do you even know how to steal?")

        if amount < 0:
            raise InvalidCommand("Amount can't be negative!")

        await burn_balance(server_id, user_id, amount)

        msg = "<@{}> just burned ${} :fire: :fire: :fire:"

        return msg.format(user_id, format_int(amount))
