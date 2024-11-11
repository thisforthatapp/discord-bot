# bots/nfts_bot.py
class NFTsBot(BaseStatsBot):
    def __init__(self):
        super().__init__("NFTs")

    async def get_count(self):
        response = self.supabase.table('nfts').select('*', count='exact').execute()
        return response.count

    async def get_emoji(self):
        return "🎨"
