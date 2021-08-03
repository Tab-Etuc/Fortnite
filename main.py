import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from config import *
from itertools import cycle


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.all() # 啟用所有 intents
activity = discord.Game('[C] | Chelp 以資查詢')
bot = commands.Bot(
    command_prefix = Prefix, 
    owner_ids = Owner_id, 
    intents = intents
)
bot.remove_command("help")
status = cycle([
    "[C] 開發者 CC_#8844", 
    "[C] | Chelp 以資查詢", 
    "指令前綴  `C`"
])

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(activity))
  print(f'{bot.user.name}已成功上線！')
    
@tasks.loop(seconds=10)
async def status_swap():
  await bot.change_presence(
      activity = discord.Activity(
          type = discord.ActivityType.watching,
          name = (next(status))
      )
  )

for filename in os.listdir('./Commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'Commands.{filename[:-3]}')

if __name__ == "__main__":
  bot.run(TOKEN)