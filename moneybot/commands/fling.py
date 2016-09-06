from random import choice
from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import transfer_balance


class Fling(Command):
    prefix = "fling"
    
    description = "Sends the money to a randomly chosen person"
    
    examples = [
        "$fling 100 @user1 @user2 @user3",
        "$fling 100 @user1"
    ]
    

    def default(self):
        server_id = int(self.message.server.id)
        source_user_id = int(self.message.author.id)
        amount = self.parse_int(self.tokens[1])
        user_ids = []
        
        if len(self.tokens) < 3:
            raise InvalidCommand("Who are the lucky ones?")

        if amount is None:
            raise InvalidCommand("Amount must be an number!")

        for user in self.parse_user_string(self.tokens(2:]):
            destination_user_id = self.parse_user_string(user)

            if not destination_user_id:
                raise InvalidCommand("No such user!".format(user))
            
            user_ids.append(destination_user_id)
        
        lucky_user_id = choice(user_ids)

        transfer_balance(server_id, source_user_id, lucky_user_id, amount)

        word = choice(["caught", "got lucky with", "found", "won", "stumbled upon"])

        return "<@{}> {} ${}".format(lucky_user_id, word amount)




