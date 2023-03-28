"""DEV PRESET. DON'T USE ON LIVE BOTS!"""
from default_config.presets.preset_main import *
print("DISCORD.PY DEV ONLY PRESET! PLEASE CHANGE TO MAIN FOR RELEASE PURPOSES.")
prefix = '.'

print(f"[DEV] New prefix: {prefix}")
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"[DEV]TESTBOT Bot is loaded! \nUploaded cmds: {' '.join(cmd_list)}")
