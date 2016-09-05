from discord import Client
from moneybot import config

client = Client()


@client.event
async def on_ready():
    pass


@client.event
async def on_message(message):
    author = message.author.id
    server = message.server.id
    content = message.content

    print("{} said {} on {}".format(author, content, server))
    #await client.send_message(message.channel, "You sent '{}'".format(message.content))


def connect_to_discord():
    client.run(config.DISCORD_TOKEN)
