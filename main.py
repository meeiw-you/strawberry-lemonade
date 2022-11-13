import discord
#import logging


#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')




pre = ">"
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

    if message.content.startswith(pre +'h'):
        await message.channel.send('hello everybody!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send("hello!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(pre +"help"):
        await message.channel.send("none")
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(pre +"link"):
        await message.channel.send(""" https://discord.com/api/oauth2/authorize?client_id=1041338819200421888&permissions=8&scope=bot , to invite me
or if you want to come to my server , https://discord.gg/ysFzG4987s""")
client.run('MTA0MTMzODgxOTIwMDQyMTg4OA.GdDs0Y.yhO6cS28SCLhgFR7jANq44juMOcTgFXrftSfeA')#,log_handler=handler, log_level=logging.DEBUG)
