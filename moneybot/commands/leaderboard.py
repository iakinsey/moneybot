from moneybot.command import Command
from moneybot.ledger import get_leaderboard


class Leaderboard(Command):
    prefix = "leaderboard"
    description = "The Fortune 500 of Discord"
    examples = [
        "$leaderboard"
    ]

    async def default(self):
        server_id = int(self.message.server.id)
        leaderboard = await get_leaderboard(server_id)
        count = 0
        rows = []

        for user_id, amount in leaderboard:
            count += 1
            rows.append("{}. ${} <@{}>".format(count, amount, user_id))

        return "**The Wealthiest**\n{}".format("\n".join(rows))
