import discord
from discord import app_commands
import asyncio
from datetime import datetime, timedelta
import pytz
import os
import json
from dotenv import load_dotenv

# Load .env file for the token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CACHE_FILE = "countdown_cache.json"

# Proper timezone-aware release time (Phoenix time)
phoenix = pytz.timezone("America/Phoenix")
release_time = phoenix.localize(datetime(2025, 8, 21, 21, 0))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

def get_countdown_text():
    """Get the current countdown text with exact days, hours, minutes, and seconds"""
    now = datetime.now(phoenix)
    delta = release_time - now
    
    if delta.total_seconds() > 0:
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60
        return f"{days}d {hours}h {minutes}m {seconds}s until Mac Demarco's \"Guitar\" Album!"
    else:
        return "Mac Demarco's Guitar Album is out now!"

async def update_status():
    await client.wait_until_ready()
    cache = load_cache()
    last_status = cache.get("status")

    while not client.is_closed():
        now = datetime.now(phoenix)
        delta = release_time - now

        if delta.total_seconds() > 0:
            days = delta.days
            hours = delta.seconds // 3600
            status = f"{days}d {hours}h until Mac Demarco's \"Guitar\" Album!"
        else:
            status = "Mac Demarco's Guitar Album is out now!"

        if status != last_status:
            await client.change_presence(activity=discord.Game(name=status))
            save_cache({"status": status})
            print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Updated status to: {status}")
            last_status = status

        # Sleep until the top of the next hour
        next_hour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        sleep_seconds = (next_hour - now).total_seconds()
        await asyncio.sleep(sleep_seconds)

@tree.command(name="countdown", description="Get the exact countdown to Mac DeMarco's Guitar album")
async def countdown_command(interaction: discord.Interaction):
    countdown_text = get_countdown_text()
    embed = discord.Embed(
        title="🎸 Mac DeMarco - Guitar Album Countdown",
        description=countdown_text,
        color=0x00ff00 if "out now" in countdown_text else 0xff6b6b
    )
    embed.set_footer(text="Release Date: August 21, 2025 at 9:00 PM Phoenix Time")
    await interaction.response.send_message(embed=embed)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync()
    client.loop.create_task(update_status())

client.run(TOKEN)
