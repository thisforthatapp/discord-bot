# deploy.sh
#!/bin/bash
set -e

echo "Deploying NFT Stats Discord Bots..."

# Clone repository
git clone https://github.com/thisforthat/discord-bot.git
cd discord-bot

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copy .env file
cp .env.example .env
echo "Please edit .env file with your credentials"

# Copy service files
sudo cp systemd/*.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Start and enable services
sudo systemctl enable users-bot nfts-bot offers-bot
sudo systemctl start users-bot nfts-bot offers-bot

echo "Deployment complete! All bots should be running."