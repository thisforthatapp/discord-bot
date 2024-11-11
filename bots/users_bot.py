# bots/users_bot.py
class UsersBot(BaseStatsBot):
    def __init__(self):
        super().__init__("users")

    async def get_count(self):
        response = self.supabase.table('users').select('*', count='exact').execute()
        return response.count

    async def get_emoji(self):
        return "👥"