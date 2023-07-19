
# Imports 
import discord
import os

import openai

# OpenAI key Setup 
openai.api_key ="***********************************************"
# Discord Key Setup 
token="***************************************"

# Discord 
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        if self.user!=message.author:
           if self.user in message.mentions:
               channel=message.channel
               # OpenAI 
               response = openai.Completion.create(
               model="text-davinci-003",
               prompt=message.content,
               temperature=0.9,
               max_tokens=900,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
               )
               messageToSend=response.choices[0].text
               await channel.send(messageToSend)
        
        
        
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)


