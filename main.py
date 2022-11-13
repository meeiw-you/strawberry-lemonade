import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>h'):
        await message.channel.send('hello everybody!')

client.run('MTA0MTMzODgxOTIwMDQyMTg4OA.GFLlIs.vYp5kvR8M8kDNISECb2GKF8jE7DcxDRQCWEg5k')