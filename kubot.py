# bot.py
import nest_asyncio
nest_asyncio.apply()
import discord
from discord.ext import commands
import numpy as np

TOKEN = 'NjMyMzA1NjE0ODg5OTQzMDgx.XaD7tw.Q6lRb3xC82uZbFUUu7JQHUABWN0'

client = discord.Client()

fourthdownrules = ('''You may go for 4th down and 3 or less from your own 40, no matter the score or quarter. 
When losing
- if you are losing by 3+ scores in the first half you can go for it anywhere
- if you are losing by 2+ scores in the second half you can go for it anywhere
- If you are losing by any score in the fourth quarter you can go for it anywhere
When winning by one score in the 4th quarter
- If you are winning by one score in the 4th quarter, you can go for it anywhere (at your own risk)
        ''')
trae = 'https://cdn.discordapp.com/attachments/438820325237456896/601070407445119006/txykwus1dqa31.png'

custom_commands = {
    '!4thdown': fourthdownrules,
    '!icetrae': trae
}

customCommands = np.array([['!hiworld', 'Hello world'],])

option1 = []
option2 = []

@client.event
async def on_message(message):
    global option1
    global option2
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        channel = message.channel
        await channel.send(msg)

    elif message.content.startswith('!addcom'):
        
        split_content = message.content.split()
        
        if len(split_content) >= 3:     
            if split_content[1] in custom_commands:
                await message.channel.send('command already exists')
            elif split_content[1].startswith('!'):
                custom_commands[split_content[1]] = ' '.join(split_content[2:])
                await message.channel.send('Command ' + str(split_content[1]) + ' add with a response of ' + str(' '.join(split_content[2:])))
            commandpadcsv = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)
            print(commandpadcsv.shape)
            print(commandpadcsv)
            caller = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)[:,0]
            #response = np.array([], dtype=str)
            response = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)[:,1]
            caller = np.append(caller, [split_content[1]])
            print(caller.shape)
            print('caller is: ', caller)
            responses = str(' '.join(split_content[2:]))
            responses = responses.replace(',', '')
            print('responses is: ', responses)
            response = np.append(response, responses)
            print(response.shape)
            print('response is: ', response)
            customCommandsPls = np.column_stack((caller, response))
            
            print(customCommandsPls)
            
            np.savetxt("commandpad.csv", customCommandsPls, delimiter=",", fmt='%s')
    
        else:
            await message.channel.send('formatting error for !addcom')
    
    elif message.content.startswith('!'):
        split_content = message.content.split()
        #commandpadcsv = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)
        callerz = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)[:,0]
        responsez = np.loadtxt('commandpad.csv', delimiter=',', dtype=str)[:,1]
        responsesz = str(' '.join(split_content[2:]))
        responsez = np.append(responsez, responsesz)
        callerz = callerz.tolist()
        responsez = responsez.tolist()
        if split_content[0] in callerz:
            await message.channel.send(responsez[callerz.index(split_content[0])])
            
    
    elif message.content.startswith('option 1') or message.content.startswith('Option 1'):
        option1.append(message.author.name)
    elif message.content.startswith('option 2') or message.content.startswith('Option 2'):
        option2.append(message.author.name)
    
    if message.content.startswith('!option') or message.content.startswith('!Option'):
        if message.content.startswith('!option1') or message.content.startswith('!Option1'):
            await message.channel.send(option1)
        if message.content.startswith('!option2') or message.content.startswith('!Option2'):
            await message.channel.send(option2)
    if message.content.startswith('!clearoptions'):
        option1 = []
        option2 = []

        
   
    #await message.channel.send(message.author)
'''    
    for command in custom_commands.keys():
        if message.content.startswith(command):
            await message.channel.send(custom_commands[command])
'''
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#bot.run(TOKEN)
client.run(TOKEN)