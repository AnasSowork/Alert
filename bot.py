import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

TOKEN = os.getenv("DISCORD_BOT_TOKEN") 

TARGET_USER_ID = 289916689980850177  
MY_USER_ID = 858663644068708374    

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🚀 ALERT Bot is online as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id == TARGET_USER_ID:
        user_to_notify = await bot.fetch_user(MY_USER_ID)
        if user_to_notify:
            alert_text = (
                f"⚡ **ALERT**: {message.author} just posted in "
                f"**{message.guild.name}** ({message.channel.name})!\n"
                f"**Message**: {message.content}"
            )
            try:
                await user_to_notify.send(alert_text)
            except Exception as e:
                print(f"Failed to send alert: {e}")
    
    # Allow commands to be processed if we are going to add them later
    await bot.process_commands(message)

if __name__ == "__main__":
    if not TOKEN:
        print("Please set DISCORD_BOT_TOKEN in your .env file!")
    else:
        bot.run(TOKEN)
