<h1 align="center">Discord.py </h1>
<h2><img src="https://i.redd.it/yhqy2c4mbkyz.gif" height="30px"> · Código </h2>

```python
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
```
