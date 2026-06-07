import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from python_aternos import Client
from mcstatus import JavaServer
import sys
import os
import asyncio
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

client = Client()
client.login("YOUR_ATERNOS_USER", "YOUR_ATERNOS_PASSWORD")
account = client.account
servers = account.list_servers()

server = servers[0] if servers else None

server_status = JavaServer.lookup("yourserver.aternos.me")

@bot.event
async def on_ready():
    print(f"Bot Is Active Users are now permitted to start the server, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "start the server" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} Please use `!start` to start the server.")

    await bot.process_commands(message)

@bot.command()
async def start(ctx):
    try:
        status = await asyncio.to_thread(server_status.status)
        await ctx.reply(f"Server Is Currently Online With {status.players.online} players.")
    except Exception:
        await ctx.reply(f"@everyone Server Is Starting... Server Started by: {ctx.author.mention}")
        if server:
            server.start()

@bot.command()
async def stop(ctx):
    await ctx.reply(f"@everyone Server Is Stopping... Server Suspended by: {ctx.author.mention}")
    if server:
        server.stop()

@bot.command()
async def restart(ctx):
    await ctx.reply(f"@everyone Server Is Restarting... Server Reset By: {ctx.author.mention}")
    if server:
        server.stop()
    if server:
        server.start()

@bot.command()
async def status(ctx):
    await ctx.reply("Checking server status...")
    try:
        status = await asyncio.to_thread(server_status.status)
        await ctx.reply(f"Server is online with {status.players.online} players.")
    except Exception:
        await ctx.reply("Server is Currently Offline, If you would like to start the server please run the !start command")

@bot.command()
async def shutdown(ctx):
    await ctx.reply(f"Shutting Down... Killed by {ctx.author.mention}")
    sys.exit()

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
