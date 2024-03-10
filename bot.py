import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = command.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def compile(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        file_path = f""

        await attachment.save(file_path)

        try:
            subprocess.run(["python", "main.py"], check=True)
            await ctx.send('File compilation successful")

            fileName_split = os.path.splittext(attachment.filename)[0]
            pdf_file = fileName_split + ".pdf"

            await ctx.send(file=discord.File(pdf_file)

        except subprocess.CalledProcessError as e:
            await ctx.send(f"File compilation failed. Error: {e}")

bot.run(TOKEN)
