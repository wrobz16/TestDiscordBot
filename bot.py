#
# created by: wrobz16
# date:       6/6/2022
#
# Test Discord Bot
#

import discord
import os

client = discord.Client()
TOKEN = 'OTgzNDA4MDM2NTMyMDg0NzQ3.G6_cP7.R_dQRbqzH-qkUZkfBmDu8wEAovr5pEduNmSSKk'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == "monkey":
        await message.channel.send('Fuck you ' + message.author.mention)

client.run(TOKEN)