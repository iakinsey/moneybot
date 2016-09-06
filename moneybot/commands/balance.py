from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import get_user_balance


class Balance(Command):
    prefix = "balance"
    description = "Get user balance"
    examples = ["$balance"]

    async def default(self):
        server_id = int(self.message.server.id)

        if len(self.tokens) == 2:
            user_id = self.parse_user_string(self.tokens[1])
        else:
            user_id = int(self.message.author.id)

        if user_id is None:
            raise InvalidCommand("No such user!")

        balance = await get_user_balance(server_id, user_id)

        if balance == 0:
            return "<@{}>'s balance is: $0. You're broke lol!".format(user_id)
        else:
            return "<@{}>'s balance is: ${}".format(user_id, balance)
