from moneybot.command import Command, get_help, alias
from moneybot.exc import InvalidCommand
from moneybot.ledger import burn_balance
from moneybot.util import format_int


PRICES = {
    "motd": 1000,
    "airhorn": 100,
    "color": 1000,
    "plunder": 5000,
    "status": 10000,
    "price": 0
}


class Buy(Command):
    prefix = "buy"
    description = "Buy things in the moneybot store."
    examples = ["$buy {}".format(i) for i in PRICES]
    _help = None

    async def default(self):
        return "Gotta buy something kid."

    @alias("price", top=True)
    async def price(self):
        if len(self.tokens) < 3:
            raise InvalidCommand("Improperly formatted command!")

        item = self.tokens[2]
        price = PRICES.get(item)

        if price is None:
            raise InvalidCommand("No such item exists in the store.")
        elif item == "price":
            raise InvalidCommand("Price queries are free")

        return "The price for {} is {}".format(item, format_int(price))

    @alias("motd", top=True)
    async def motd(self):
        cost = PRICES['motd']
        balance = await self.get_balance()

        if balance < cost:
            raise InvalidCommand("You're too poor, lol.")

        if len(self.tokens) < 3:
            raise InvalidCommand("Improperly formatted command!")

        topic = " ".join(self.tokens[2:])

        await self.client.edit_channel(self.message.channel, topic=topic)
        await burn_balance(self.server_id, self.author_id, cost)

    @alias("airhorn", top=True)
    async def airhorn(self):
        raise NotImplementedError

    @alias("color", top=True)
    async def color(self):
        cost = PRICES['color']

    @alias("plunder", top=True)
    async def plunder(self):
        cost = PRICES['plunder']

    @alias("status", top=True)
    async def status(self):
        cost = PRICES['status']
