# 1. Clone the repository

cd /home/ubuntu
git clone https://github.com/thisforthat/discord-bot.git
cd discord-bot

# 2. Set up Python virtual environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Create and configure .env file

cp .env.example .env
nano .env

# Add your tokens and URLs:

# SUPABASE_URL=your_url

# SUPABASE_KEY=your_key

# USERS_BOT_TOKEN=your_token

# NFTS_BOT_TOKEN=your_token

# OFFERS_BOT_TOKEN=your_token

# 4. Set correct permissions

chmod 600 .env

# 5. Install systemd services

# Copy each service file

sudo cp systemd/users-bot.service /etc/systemd/system/
sudo cp systemd/nfts-bot.service /etc/systemd/system/
sudo cp systemd/offers-bot.service /etc/systemd/system/

# 6. Start the services

sudo systemctl daemon-reload
sudo systemctl enable users-bot nfts-bot offers-bot
sudo systemctl start users-bot nfts-bot offers-bot

# 7. Check status

sudo systemctl status users-bot nfts-bot offers-bot

# Reload systemd

sudo systemctl daemon-reload

# Check their status

sudo systemctl status users-bot
