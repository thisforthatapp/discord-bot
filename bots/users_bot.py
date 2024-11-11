import os
from base_bot import BaseStatsBot

class UsersBot(BaseStatsBot):
    def __init__(self):
        super().__init__("users")

    async def get_count(self):
        response = self.supabase.table('user_profile').select('*', count='exact').execute()
        return response.count

    async def get_emoji(self):
        return "👥"

if __name__ == "__main__":
    bot = UsersBot()
    bot.run(os.getenv('USERS_BOT_TOKEN'))