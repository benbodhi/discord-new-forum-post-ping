import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables for bot token, guild ID, forum channel ID, and role name
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
FORUM_CHANNEL_ID = os.getenv('FORUM_CHANNEL_ID')
ROLE_NAME = os.getenv('ROLE_NAME')

# Define the necessary intents - we're listening to messages and their content
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Initialize the bot with the specified command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """
    This function runs when the bot starts up and logs its name.
    """
    logger.info(f"Logged in as {bot.user.name}!")

@bot.event
async def on_message(message):
    """
    This function runs every time a message is posted in the server.
    If the message's channel is a child of the main forum channel, the bot responds.
    """
    if not message.author.bot:  # Ensure the message is not from a bot
        # If the message's channel parent matches our forum channel ID
        if message.channel.parent_id == int(FORUM_CHANNEL_ID):
            guild = discord.utils.get(bot.guilds, id=int(GUILD_ID))
            role = discord.utils.get(guild.roles, name=ROLE_NAME)
            await message.channel.send(f"New {role.mention} episode in the works.")
        else:
            logger.debug(f"Message detected from {message.author.name} in channel {message.channel.id}. Ignoring.")

    # Process any commands that might be in the message (though in this case, you don't have any specific commands)
    await bot.process_commands(message)

# Run the bot using the token from the environment variable
bot.run(TOKEN)
