import discord

sl = "strawberry lemonade"
pre = ">"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(pre +"link"):
        await message.channel.send(""" https://discord.com/api/oauth2/authorize?client_id=1041338819200421888&permissions=8&scope=bot , to invite me
or if you want to come to my server , https://discord.gg/ysFzG4987s.""")

    if message.content.startswith(pre +"help"):
        await message,channel.send("i so sorry none.")

    if message.content.startswith(pre +'h'):
        await message.channel.send('hello everybody!')

    if message.content.startswith("hi"):
        await message.channel.send("hello!")

    if message.content.startswith(pre +"help"):
        await message.channel.send("i so sorry none.")

    if message.content.startswith(sl + " how are you"):
        await message.channel.send("i very fine. you ?")

    if message.content.startswith(sl + " help me"):
        await message.channel.send("i can how help ?")
    if message.content.startswith(sl + " who wrote your software"):
        await message.channel.send("""discord name: 'meiw you'#2200
        , github name: meeiw-you
        , github profil link: https://github.com/meeiw-you
        , discord server: https://discord.gg/ysFzG4987s""")
client.run('MTA0MTMzODgxOTIwMDQyMTg4OA.GFBstl.bXwU5GQsw0nrM7zezhFeiJSX9Lh6OZzAhqPd5g')

