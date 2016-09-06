from moneybot.command import Command


class Help(Command):
    prefix = "help"

    def default(self):
        return "You're on your own lol!"
