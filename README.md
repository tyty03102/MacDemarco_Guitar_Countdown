# Mac DeMarco Countdown Discord Bot

This Discord bot updates its status every hour with a countdown to Mac DeMarco's upcoming album "Guitar." The status shows the days and hours remaining until the release.

## Features
- Updates status every hour with a countdown to the album release
- Status format: `Xd Yh until Mac Demarcos New Album Guitar!`
- Once the album is out, status changes to: `Mac Demarcos New Album Guitar is out now!`
- `/countdown` slash command that shows the exact countdown with days, hours, minutes, and seconds
- Beautiful embed response with color-coded countdown (red for countdown, green when released)

## Commands
- `/countdown` - Get the exact countdown to Mac DeMarco's Guitar album with precise timing

## Invite My Hosted Bot
If you don't want to host your own, you can invite my running bot to your server using this link:
[Invite Mac DeMarco Countdown Bot](https://discord.com/oauth2/authorize?client_id=1387152142044893306&permissions=0&integration_type=0&scope=bot)

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/macky-dc-bot.git
cd macky-dc-bot
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Set Up Your Bot Token
Create a `.env` file in the project directory and add your Discord bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

### 4. Run the Bot
```sh
python main.py
```

## Customization
- To use your own countdown, change the `release_time` variable in `main.py`.
- The bot uses the "Watching" status type for the countdown.
- Slash commands are automatically synced when the bot starts up.

## How to Make Your Own Discord Bot
See the step-by-step guide: [How to Make a Discord Bot](HOW_TO_MAKE_A_DISCORD_BOT.md)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.