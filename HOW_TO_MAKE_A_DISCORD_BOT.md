# How to Make a Discord Bot (After Cloning This Repo)

This guide will walk you through setting up your own Discord bot using this repository. You'll create a bot in the Discord Developer Portal, configure your token, and run the bot locally.

---

## 1. Create a Discord Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give it a name.
3. Go to the **Bot** tab and click **Add Bot**.
4. (Optional) Set your bot's avatar and username.

## 2. Get Your Bot Token
1. In the **Bot** tab, click **Reset Token** and copy the token.
2. **Keep this token secret!** Anyone with it can control your bot.

## 3. Invite Your Bot to a Server
1. Go to the **OAuth2 > URL Generator** tab.
2. Under **Scopes**, select `bot`.
3. Under **Bot Permissions**, select the permissions your bot needs (for basic status updates, no permissions are required).
4. Copy the generated URL and open it in your browser to invite the bot to your server.

## 4. Set Up Your Bot Token Locally
1. In the project directory, create a `.env` file (or copy `sample env` to `.env`).
2. Paste your bot token in the file like this:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```
## **UPDATE YOUR NEW BOT TOKEN WITH THIS ONE HERE**

## 5. Install Dependencies
Make sure you have Python 3.8 or higher installed. Then run:
```sh
pip install -r requirements.txt
```

## 6. Run the Bot
```sh
python main.py
```

Your bot should now be online in your server!

---

## Resources
- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications) 