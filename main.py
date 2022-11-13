import discord
#import logging


#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')



sl = "strawberry lemonade"
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
    if message.content.startswith(pre +"link"):# link
        await message.channel.send(""" https://discord.com/api/oauth2/authorize?client_id=1041338819200421888&permissions=8&scope=bot , to invite me
or if you want to come to my server , https://discord.gg/ysFzG4987s.""")

    if message.content.startswith(pre +'h'):#herkese selam ver
        await message.channel.send('hello everybody!')

    if message.content.startswith("hi"):#selam
        await message.channel.send("hello!")

    if message.content.startswith(pre +"help"):#>yardım
        await message.channel.send("i so sorry none.")

    if message.content.startswith(sl + " how are you"):#çilekli limonata nasılsın
        await message.channel.send("i very fine. you ?")

    if message.content.startswith(sl + " help me"):# çilekli limonata yardım et
        await message.channel.send("i can how help ?")

    if message.content.startswith(sl + " who wrote your software"):#cilekli limonatayi kim yazdı
        await message.channel.send("""discord name: 'meiw you'#2200
        , github name: meeiw-you
        , github profil link: https://github.com/meeiw-you
        , discord server: https://discord.gg/ysFzG4987s""")

    if message.content.startswith(sl +" open new page"):#yeni sayfa
        await message.channel.send("""...



















































































































        """)

client.run('MTA0MTMzODgxOTIwMDQyMTg4OA.GFBstl.bXwU5GQsw0nrM7zezhFeiJSX9Lh6OZzAhqPd5g')#,log_handler=handler, log_level=logging.DEBUG)
