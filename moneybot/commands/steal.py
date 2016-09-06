from moneybot.command import Command


class Steal(Command):
    prefix = "steal"

    def default(self):
        return "Not ready just yet!"
