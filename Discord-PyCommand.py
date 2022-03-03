@client.event
async def on_ready():
    print('He iniciado sessión en: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?help'):
        await message.channel.send('Hola! Soy Panda Bot')
      

client.run('TU_TOKEN') # Para saber que Token tienes dirigete a = https://discord.com/developers/applications
