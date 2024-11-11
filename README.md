# NFT Stats Discord Bots 🤖

This repository contains three Discord bots that display real-time statistics from your NFT platform's Supabase database. Each bot focuses on a specific metric and updates its status every 15 minutes.

## Features 📊

- **Users Bot** 👥

  - Displays total number of users
  - Updates every 15 minutes
  - Shows error status when database is unreachable

- **NFTs Bot** 🎨

  - Shows total NFTs in the platform
  - Updates every 15 minutes
  - Auto-recovers from errors

- **Offers Bot** 💰
  - Tracks total number of offers made
  - Updates every 15 minutes
  - Independent operation from other bots

## Prerequisites 📋

- Python 3.8+
- A Linux server (e.g., Ubuntu on GCP)
- Three Discord bot tokens
- Supabase account and credentials

## Setup Guide 🚀

### 1. Discord Bot Creation

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create three new applications (one for each metric)
3. For each application:
   - Go to the "Bot" section
   - Click "Reset Token" and copy the token
   - Disable "Public Bot"
   - Enable "Presence Intent"
   - Add bot to your server using OAuth2 URL Generator (Bot scope only)

### 2. Environment Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nft-discord-bots.git
cd nft-discord-bots
```

2. Copy and configure environment variables:

```bash
cp .env.example .env
```

3. Edit `.env` with your credentials:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
USERS_BOT_TOKEN=your_users_bot_token
NFTS_BOT_TOKEN=your_nfts_bot_token
OFFERS_BOT_TOKEN=your_offers_bot_token
```

### 3. Deployment

Run the deployment script:

```bash
chmod +x deploy.sh
./deploy.sh
```

This will:

- Set up a Python virtual environment
- Install required packages
- Configure systemd services
- Start all bots

## File Structure 📁

```
discord-bot/
├── .env.example
├── requirements.txt
├── deploy.sh
├── bots/
│   ├── base_bot.py
│   ├── users_bot.py
│   ├── nfts_bot.py
│   └── offers_bot.py
└── systemd/
    ├── users-bot.service
    ├── nfts-bot.service
    └── offers-bot.service
```

## Management Commands 🛠

### Check bot status:

```bash
sudo systemctl status users-bot
sudo systemctl status nfts-bot
sudo systemctl status offers-bot
```

### Restart bots:

```bash
sudo systemctl restart users-bot
sudo systemctl restart nfts-bot
sudo systemctl restart offers-bot
```

### View logs:

```bash
sudo journalctl -u users-bot -f
sudo journalctl -u nfts-bot -f
sudo journalctl -u offers-bot -f
```

## Updating 🔄

1. Pull latest changes:

```bash
git pull
```

2. Restart services:

```bash
sudo systemctl restart users-bot nfts-bot offers-bot
```

## Troubleshooting 🔍

### Bot shows "DND" (red) status:

- Check Supabase connection
- Verify database permissions
- Review logs for errors

### Bot is offline:

```bash
# Check service status
sudo systemctl status [bot-name]

# Check logs
sudo journalctl -u [bot-name] -n 50
```

### Common Issues:

1. **Invalid Token**: Verify bot tokens in `.env`
2. **Database Connection**: Check Supabase URL and key
3. **Permission Issues**: Ensure proper file permissions
4. **Network Issues**: Check firewall settings

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License 📝

MIT License - feel free to use this code in your own projects!

## Support 💬

For issues and feature requests, please create a GitHub issue with:

- Description of the problem/request
- Steps to reproduce (for issues)
- Relevant logs or screenshots
