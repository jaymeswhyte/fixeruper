from dotenv import load_dotenv
import os
import discord

# Environment variables
load_dotenv()
TOKEN = os.environ["TOKEN"]
GUILD_ID = int(os.environ["GUILD_ID"])
GUILD_OBJECT = discord.Object(id=GUILD_ID)
client = discord.Client(intents=discord.Intents.default())

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "//x.com" in message.content:
        fixed_message = message.content.replace("//x.com", "//fixupx.com")
        await message.delete()

        kwargs = {
            "content": f"{message.author.mention}:\n{fixed_message}"
        }

        # Handle Replies
        if message.reference:
            try:
                replied_to = await message.channel.fetch_message(message.reference.message_id)
                kwargs["reference"] = replied_to
                kwargs["mention_author"] = False 
            except discord.NotFound:
                pass # Ignore if message not found

        await message.channel.send(**kwargs)

client.run(TOKEN)