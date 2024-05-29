# main.py

import discord
from discord.ext import commands
from commands import moderation_commands, role_commands, reminder_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Add commands from different modules
bot.add_cog(moderation_commands.ModerationCommands(bot))
bot.add_cog(role_commands.RoleCommands(bot))
bot.add_cog(reminder_commands.ReminderCommands(bot))

# Run the bot
bot.run('YOUR_DISCORD_TOKEN')