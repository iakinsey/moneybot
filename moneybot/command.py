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
    description = None
    examples = []

    def __init__(self, client, message, contents, tokens):
        self.client = client
        self.message = message
        self.contents = contents
        self.tokens = tokens

    async def perform(self):
        return await self.default()

    async def default(self):
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

    @property
    def user_is_admin(self):
        pass

    @property
    def addressing_me(self):
        pass


def get_command(name):
    command = COMMANDS.get(name)

    if not command:
        raise InvalidCommand("No such command!")

    return command


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


def get_help():
    return [{
        "name": Command.prefix,
        "description": Command.description,
        "examples": Command.examples
    } for name, Command in COMMANDS.items()]
