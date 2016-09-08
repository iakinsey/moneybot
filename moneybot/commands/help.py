from moneybot.command import Command, get_help


class Help(Command):
    prefix = "help"
    description = "Get help."
    examples = [
        "$help",
        "$help pay",
        "$help fedspeak"
    ]
    _help = None

    async def default(self):
        await self.client.send_message(self.message.author, self.help)

    @property
    def help(self):
        if self._help is not None:
            return self._help

        info = get_help()
        response = [
            "**GET HELPED**",
            "Prefix all commands with $\n"
        ]

        for item in info:
            header = "**{}** - {}".format(item['name'], item['description'])

            if item['examples']:
                examples = "```{}```".format("\n".join(item['examples']))
            else:
                examples = ""

            msg = "{}\n{}".format(header, examples)
            response.append(msg)

        self._help = "\n".join(response)

        return self._help
