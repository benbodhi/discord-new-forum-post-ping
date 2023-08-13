# discord-new-forum-post-ping

Pings a specified role when a new post is created in a forum.

## Overview

This Discord bot is designed to post a message and ping a specified role whenever a new post is created in a designated forum within a server. The bot uses the Python Discord API and is easily customizable for different roles and forum channels by setting them in the environment variables.

## Features

- Automated pings for a specified role when a new forum post is created.
- Logging for debugging and monitoring.
- Environment variable based configuration for enhanced security.

## Requirements

- Python 3.x
- Discord API Token
- Python packages: `discord`, `python-dotenv`, `logging`

## Discord Bot Setup

1. **Create a Discord Application**

    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Click the "New Application" button and give it a name.
    - On the left sidebar, click on "Bot" and then click "Add Bot".

2. **Set Up Bot Permissions**

   - While in the Bot tab, under the "Privileged Gateway Intents" section, enable "PRESENCE INTENT", "SERVER MEMBERS INTENT" and "MESSAGE CONTENT INTENT".
   - Under the "TOKEN" section, click "Copy" to copy your bot token for use later - you may need to click "Reset Token" first.

3. **Invite the Bot to Your Server**

   - On the left sidebar, click on "OAuth2".
   - Under the "OAuth2" > "URL Generator" section, select the "bot" scope.
   - Select the permissions your bot needs. At a minimum, it will need "Read Messages/View Channels", "Send Messages", "Send Messages in Threads", "Read Message History" and "Mention Everyone".
   - Copy the generated URL and open it in a web browser to invite the bot to your server.
   - Now in Discord, either add the bot to the forums/channels you need it for, or give the bot a role that gives it access to them, or update the bot's role permissions to suit.

## Local Setup & Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/benbodhi/discord-new-forum-post-ping.git
   cd discord-new-forum-post-ping
   ```

2. **Set Up a Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install discord.py python-dotenv
   ```

4. **Environment Variables**

   First, ensure you have Discord's Developer Mode enabled to easily copy IDs. To enable it:
   - Open Discord and go to your User Settings (the gear icon next to your username in the bottom left).
   - In the Appearance tab, scroll down and toggle on 'Developer Mode'.

   With Developer Mode enabled, you can now right-click on servers, channels, users, or messages to obtain their respective IDs by selecting 'Copy ID'.

   Create a `.env` file in the root directory and set the following:

   - `DISCORD_TOKEN`: Your bot's token from the Discord Developer Portal.
   - `GUILD_ID`: Right-click on your server's icon (with Developer Mode enabled) and select 'Copy ID'.
   - `FORUM_CHANNEL_ID`: Navigate to the desired forum channel in Discord, right-click on its name, and select 'Copy ID'.
   - `ROLE_NAME`: The name of the role you wish to mention. Ensure this role exists in your server.

   Your `.env` file should look something like this:

   ```js
   DISCORD_TOKEN=your_discord_token
   GUILD_ID=your_guild_id
   FORUM_CHANNEL_ID=your_forum_channel_id
   ROLE_NAME=YourRoleNameHere
   ```

   Remember to include `.env` in your `.gitignore` to prevent exposing sensitive information.

5. **Run the Bot**

   ```bash
   python pinger.py
   ```

## Customization

To customize the role or forum channel, adjust the `ROLE_NAME` and `FORUM_CHANNEL_ID` variables in your `.env` file.
