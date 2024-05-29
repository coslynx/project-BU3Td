import discord
from discord.ext import commands

# Import other modules from the project
from commands.moderation_commands import *
from commands.role_commands import *
from commands.reminder_commands import *
from filters.message_filters import *
from filters.content_filters import *
from actions.moderation_actions import *
from actions.role_actions import *
from integrations.third_party_integration import *
from logging.moderation_logs import *

# Create a new Discord bot
bot = commands.Bot(command_prefix='!')

# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Event to run when a message is received
@bot.event
async def on_message(message):
    # Check for inappropriate content
    if check_content(message.content):
        await message.delete()
        await message.channel.send('Inappropriate content detected and removed.')
    
    await bot.process_commands(message)

# Add commands related to moderation, roles, and reminders
bot.add_command(warn)
bot.add_command(kick)
bot.add_command(ban)
bot.add_command(assign_role)
bot.add_command(remove_role)
bot.add_command(set_reminder)

# Run the bot with the specified token
bot.run('YOUR_DISCORD_BOT_TOKEN')