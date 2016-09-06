from moneybot.command import Command


class Steal(Command):
    prefix = "steal"
    description = "Steal money from users."
    examples = [
        "$steal @Moneybot 100",
        "$steal @user 9001"
    ]

    async def default(self):
        return "Not ready just yet!"
