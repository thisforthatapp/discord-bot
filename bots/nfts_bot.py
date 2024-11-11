import os
from base_bot import BaseStatsBot

class NFTsBot(BaseStatsBot):
    def __init__(self):
        super().__init__("NFTs")

    async def get_count(self):
        response = self.supabase.table('nfts').select('*', count='exact').execute()
        return response.count

    async def get_emoji(self):
        return "🖼️"

if __name__ == "__main__":
    bot = NFTsBot()
    bot.run(os.getenv('NFTS_BOT_TOKEN'))