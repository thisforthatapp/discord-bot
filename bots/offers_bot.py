# bots/offers_bot.py
class OffersBot(BaseStatsBot):
    def __init__(self):
        super().__init__("offers")

    async def get_count(self):
        response = self.supabase.table('offers').select('*', count='exact').execute()
        return response.count

    async def get_emoji(self):
        return "🤝"

if __name__ == "__main__":
    bot = OffersBot()
    bot.run(bot.supabase_key)