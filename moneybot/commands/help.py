from moneybot.command import Command, get_help


class Help(Command):
    prefix = "help"
    description = "Get help."
    examples = [
        "$help",
        "$help pay",
        "$help fedspeak"
    ]

    async def default(self):
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

        await self.client.send_message(self.message.author, "\n".join(response))

        return (
            "Can't get filthy rich without some help! "
            "You've received a PM containing information."
        )
