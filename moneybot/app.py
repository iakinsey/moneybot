from discord import Client
from moneybot import config
from moneybot.exc import InvalidCommand, MoneybotException
from moneybot.ledger import update_balance, get_user_balance, transfer_balance
import discord


client = Client()


def get_contents(message):
    if message.content.startswith("$"):
        return message.content.strip("$").strip()
    if message.content.startswith("<@"):
        mentions = message.mentions

        if not mentions:
            return False

        mention_id = message.mentions[0].id
        me = message.server.me.id
        template = "<@{}>".format(me)

        if message.content.startswith(template):
            return message.content.replace(template, "").strip()

    return False


@client.event
async def on_message(message):
    try:
        await process_message(message)
    except MoneybotException as e:
        if e.args and e.public:
            await client.send_message(message.channel, e.args[0])
        else:
            raise
    except Exception:
        raise


async def process_message(message):
    author = message.author.id
    server = message.server.id
    contents = get_contents(message)

    if contents:
        fn, tokens = get_command(contents)

        response = fn(message, tokens)

        if response:
            await client.send_message(message.channel, response)


def get_command(contents):
    fns = {
        "send": send,
        "balance": balance,
        "help": help
    }

    tokens = contents.split()

    if not tokens:
        raise InvalidCommand("Invalid command!")

    if tokens:
        command = tokens[0]

    fn = fns.get(command)

    if not fn:
        raise InvalidCommand("Invalid command!")

    return fn, tokens


def parse_user_string(user_str):
    if "!" in user_str:
        cleaned = user_str.replace("<@!", "").replace(">", "")
    else:
        cleaned = user_str.replace("<", "").replace(">", "").replace("@", "")

    return parse_int(cleaned)


def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def send(message, tokens):
    server_id = int(message.server.id)
    source_user_id = int(message.author.id)

    if len(tokens) != 4:
        raise InvalidCommand("Send command was not formatted properly!")

    amount = parse_int(tokens[1])

    if amount is None:
        raise InvalidCommand("Amount must be an number!")

    destination_user_id = parse_user_string(tokens[3])

    if not destination_user_id:
        raise InvalidCommand("No such user!")

    transfer_balance(server_id, source_user_id, destination_user_id, amount)

    return "Sent ${} to <@{}>".format(amount, destination_user_id)


def balance(message, tokens):
    server_id = int(message.server.id)

    if len(tokens) == 2:
        user_id = parse_user_string(tokens[1])
    else:
        user_id = int(message.author.id)

    if user_id is None:
        raise InvalidCommand("No such user!")

    balance = get_user_balance(server_id, user_id)

    if balance == 0:
        return "<@{}>'s balance is: $0. You're broke lol!".format(user_id)
    else:
        return "<@{}>'s balance is: ${}".format(user_id, balance)


def help(message, tokens):
    pass


def connect_to_discord():
    client.run(config.DISCORD_TOKEN)
