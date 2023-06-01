import discord
from discord import Intents
import requests
import asyncio

users = ["IGN", "IGN"]
userdata = []

key = "82aae1f7-1056-4211-9018-a3840568a697"
bot_token = "TOKEN"
channel_id = "ID"

for i in range(len(users)):
    userdata.append("")
    userdata[i] = "offline"

intents = Intents.default()
intents.typing = False
intents.presences = True
intents.messages = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as", client.user.name)
    await client.change_presence(activity=discord.Game(name="Monitoring Minecraft users"))
    notify_channel = await client.fetch_channel(channel_id)
    
    while True:
        for i in range(len(users)):
            name = users[i]
            uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name).json()["id"]
            hypickle = requests.get("https://api.hypixel.net/status?key=" + key + "&uuid=" + uuid).json()

            if hypickle["session"]["online"]:
                if userdata[i] == "offline":
                    message = f"{name} is now online."
                    await notify_channel.send(message)
                    print(message)
                userdata[i] = "online"
            else:
                if userdata[i] == "online":
                    message = f"{name} has gone offline."
                    await notify_channel.send(message)
                    print(message)
                userdata[i] = "offline"

        await asyncio.sleep(10)

async def run_bot():
    await client.start(bot_token)

asyncio.run(run_bot())
