from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import transfer_balance


class Pay(Command):
    prefix = "pay"
    description = "Pay a user. Must point to a valid user."
    examples = [
        "$pay @user 100",
        "$pay @Moneybot 10000"
    ]

    async def default(self):
        server_id = int(self.message.server.id)
        source_user_id = int(self.message.author.id)

        if len(self.tokens) != 3:
            raise InvalidCommand("Send command was not formatted properly!")

        amount = self.parse_int(self.tokens[2])

        if amount is None:
            raise InvalidCommand("Amount must be an number!")

        destination_user_id = self.parse_user_string(self.tokens[1])

        if not destination_user_id:
            raise InvalidCommand("No such user!")

        transfer_balance(server_id, source_user_id, destination_user_id, amount)

        return "Sent ${} to <@{}>".format(amount, destination_user_id)
