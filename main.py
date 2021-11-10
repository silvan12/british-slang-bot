import discord
import json
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all(),
                        activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
slash = SlashCommand(client, sync_commands=True)

guild_ids = [853612274527109150]

with open("Data/slang.json") as file:
    slang = json.load(file)
