from os import name
import discord
import aiohttp
import requests
from discord_components import*
from discord import flags
from discord.ext import commands, tasks

client = commands.Bot(command_prefix=commands.when_mentioned_or('.'))