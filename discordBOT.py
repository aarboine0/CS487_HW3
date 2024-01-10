import nest_asyncio
nest_asyncio.apply()
import discord
import random
TOKEN = "MTE5MjkyOTE4MDU1NjQ4MDYzNA.Gq1TfO.8OYyjaBzl_BQDHq2ZpvrTjcWDgka0hsn1frtBI"    # you should copy your token for your bot 
client = discord.Client()

GUILD= "DATA133 testing guild"        #{your-guild-name}

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )   


@client.event
async def on_message(message):
    print(f"Message received: {message.content}")

    if message.author == client.user:
        print('Bot message - ignoring')
        return

    bot_quotes = ['Hello, I am a bot 💯 emoji.', 'Bingo!', 'happy, cool, happy, cool, happy, cool ', 'no doubt no doubt no doubt no doubt.']

    if message.content == 'wow!':
        print('Command wow! detected')
        response = random.choice(bot_quotes)
        await message.channel.send(response)
    else:
        print('Command wow! not detected')


client.run(TOKEN) #Move to bottom of script

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )



