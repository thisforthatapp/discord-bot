# bots/base_bot.py
import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from supabase import create_client, Client

class BaseStatsBot(discord.Client):
    def __init__(self, metric_name):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.metric_name = metric_name
        self.update_stats.start()
        
        # Initialize Supabase
        self.supabase = create_client(
            os.getenv('SUPABASE_URL'),
            os.getenv('SUPABASE_KEY')
        )

    async def setup_hook(self):
        print(f'{self.metric_name} bot is ready!')

    async def get_count(self):
        raise NotImplementedError("Subclasses must implement get_count()")

    async def get_emoji(self):
        raise NotImplementedError("Subclasses must implement get_emoji()")

    @tasks.loop(minutes=15)
    async def update_stats(self):
        try:
            count = await self.get_count()
            emoji = await self.get_emoji()
            
            # Update bot status
            activity = discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{count:,} {self.metric_name}"
            )
            await self.change_presence(activity=activity, status=discord.Status.online)
            
        except Exception as e:
            print(f"Error updating {self.metric_name} stats: {e}")
            await self.change_presence(status=discord.Status.dnd)

    @update_stats.before_loop
    async def before_update_stats(self):
        await self.wait_until_ready()