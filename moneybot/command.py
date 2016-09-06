from importlib import import_module
from moneybot import config
from moneybot.exc import InvalidCommand
from os import listdir


COMMANDS = {}


class Command:
    """
    Base command class.
    """

    prefix = None
    help = None

    def __init__(self, message, contents, tokens):
        self.message = message
        self.contents = contents
        self.tokens = tokens

    def perform(self):
        return self.default()

    def default(self):
        raise InvalidCommand("Invalid {} command!".format(self.prefix))

    def parse_user_string(self, user_str):
        if "!" in user_str:
            cleaned = user_str.replace("<@!", "").replace(">", "")
        else:
            cleaned = user_str.replace("<", "").replace(">", "").replace("@", "")

        return self.parse_int(cleaned)

    def parse_int(self, string):
        try:
            return int(string)
        except ValueError:
            return None


def get_command(name):
    return COMMANDS[name]


def setup_commands():
    modules = [
        import_module("moneybot.commands.{}".format(i.replace(".py", "")))
        for i in listdir(config.COMMANDS_PATH)
        if not i.startswith("_") and i.endswith(".py")
    ]

    for module in modules:
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            valid = all((
                isinstance(attr, type) and issubclass(attr, Command),
                attr != Command
            ))

            if not valid:
                continue

            if not getattr(attr, "prefix"):
                err = "Command {} requires prefix.".format(attr_name)
                raise ValueError(err)

            COMMANDS.update({attr.prefix: attr})
