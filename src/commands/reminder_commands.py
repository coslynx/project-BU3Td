# reminder_commands.py (Python)

# Import necessary packages
import discord
from discord.ext import commands
import asyncio
import datetime

# Reminder Commands
class ReminderCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='remind', help='Set a reminder with a specific message and time')
    async def remind(self, ctx, time, *, message):
        try:
            await ctx.message.delete()
            await ctx.send(f'{ctx.author.mention}, I will remind you about "{message}" in {time}.')

            # Convert time to seconds
            time_seconds = convert_time_to_seconds(time)

            # Schedule reminder
            await asyncio.sleep(time_seconds)
            await ctx.send(f'{ctx.author.mention}, Reminder: {message}')

        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

# Function to convert time to seconds
def convert_time_to_seconds(time):
    try:
        time_values = time.split()
        total_seconds = 0

        for value in time_values:
            if 's' in value:
                total_seconds += int(value[:-1])
            elif 'm' in value:
                total_seconds += int(value[:-1]) * 60
            elif 'h' in value:
                total_seconds += int(value[:-1]) * 3600
            elif 'd' in value:
                total_seconds += int(value[:-1]) * 86400

        return total_seconds

    except Exception as e:
        print(f'Error in converting time to seconds: {e}')

# Add ReminderCommands cog to the bot
def setup(bot):
    bot.add_cog(ReminderCommands(bot))