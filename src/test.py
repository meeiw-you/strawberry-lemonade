import discord


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')


client.run("MTA0MTMzODgxOTIwMDQyMTg4OA.G3v2cK.hv7luWtH8a-LmNO6ffmawaitdACGoCAHxJ22Mw")
