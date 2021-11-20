import discord
import json
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all(),
                        activity=discord.Activity(type=discord.ActivityType.listening, name="UK DRILL"))
slash = SlashCommand(client, sync_commands=True)

# Enter your guild ID here
guild_ids = []

# Enter your bot token here
token = ""

with open("Data/slang.json") as file:
    slang = json.load(file)
    
@slash.slash(name="definition",
             description="Test your British slang knowledge",
             guild_ids=guild_ids)
async def definition(ctx):
    word = random.choice(list(slang))
    _definition = slang[word]
    await ctx.send(f"\"{word}\"\n{_definition} ")
    
client.run(token)
