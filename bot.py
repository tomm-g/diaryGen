import discord
from discord.ext import commands
import os
import subprocess
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def help(ctx):
    help_message = (
        "Welcome to the Bot!\n"
        "Command List:\n"
        "!help - Display this help message.\n"
        "!process_file - Process a CSV file and send a PDF back."
    )
    await ctx.send(help_message)

@bot.command()
async def process_file(ctx):
    if not ctx.message.attachments:
        await ctx.send("No file attached.")
        return

    attached_file = ctx.message.attachments[0]
    file_path = os.path.join(os.getcwd(), attached_file.filename)

    # Check if the file is named 'template.csv' and exit early
    if attached_file.filename.lower() == 'template.csv':
        await ctx.send("This is a template file. No processing needed.")
        return

    await attached_file.save(file_path)

    try:
        # Run your other Python code here
        subprocess.run(['python3', 'main.py'], check=True)

        # Generate a PDF with the same name as the CSV file
        pdf_file_path = file_path.replace('.csv', '.pdf')

        # Send the PDF file
        pdf_file = discord.File(pdf_file_path)
        await ctx.send("File processed successfully.", file=pdf_file)

    except subprocess.CalledProcessError as e:
        await ctx.send(f"Error processing file: {e}")


bot.run(TOKEN)

