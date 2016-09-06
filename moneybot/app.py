from discord import Client
from moneybot import config
from moneybot.command import get_command
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


async def process_message(message):
    author = message.author.id
    server = message.server.id
    contents = get_contents(message)

    if contents:
        tokens = contents.split()
        Command = get_command(tokens[0])
        command = Command(message, contents, tokens)
        response = command.perform()

        if response:
            await client.send_message(message.channel, response)


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


def connect_to_discord():
    client.run(config.DISCORD_TOKEN)
