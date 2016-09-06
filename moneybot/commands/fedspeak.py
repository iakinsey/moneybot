from moneybot.command import Command
from moneybot.exc import InvalidCommand
from moneybot.ledger import transfer_balance
from random import choice


class FedSpeak(Command):
    prefix = "fedspeak"
    description = "Speak like the federal reserve!"

    options = [
        "The members of the Board of Governors and the Reserve Bank presidents foresee an implicit strengthening of activity after the current rebalancing is over, although the central tendency of their individual forecasts for real GDP still shows a substantial slowdown, on balance, for the year as a whole.",
        "I would generally expect that today in Washington DC. the probability of changes in the weather is highly uncertain, but we are monitoring the data in such a way that we will be able to update people on changes that are important.",
        "Clearly, sustained low inflation implies less uncertainty about the future, and lower risk premiums imply higher prices of stocks and other earning assets. We can see that in the inverse relationship exhibited by price/earnings ratios and the rate of inflation in the past. But how do we know when irrational exuberance has unduly escalated asset values, which then become subject to unexpected and prolonged contractions as they have in Japan over the past decade?",
        "Risk takers have been encouraged by a perceived increase in economic stability to reach out to more distant time horizons. But long periods of relative stability often engender unrealistic expectations of it[s] permanence and, at times, may lead to financial excess and economic stress.",
        "Modest preemptive action can obviate the need of more drastic actions at a later date and that could destabilize the economy.",
        "Blah blah blah blah. My words have no consequence.",
        "Something something bond markets. Something something interest rates. Something something print money!"
    ]

    async def default(self):
        return choice(self.options)
