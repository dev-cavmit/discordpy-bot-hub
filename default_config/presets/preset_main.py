from os import getenv  # .env token
from dotenv import load_dotenv
from importlib import import_module
from discord.ext import commands
from default_config.glob import *
from modules.commands_assist.pre_config import *
from modules.commands_assist.proceed import *
from modules.commands_assist.exceptions import *


_console_splash = f"[Python 3]{bot_name}: "
load_dotenv()
TOKEN = getenv(f"{bot_name.replace(' ', '_').upper()}_TOKEN")  # define bot's token

print(_console_splash + "Starting a New Discord.Py Bot, please wait...")

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')

print(_console_splash + "Configuration loaded, now starting...")


@bot.event
async def on_ready():
    print(f"{_console_splash}Bot is ready! \nCommands available: {' '.join(cmd_list)}")


@bot.event  # cmds handler
async def on_message(ctx):
    if ctx.author == bot.user or ctx.author == discord.Member.bot or not ctx.content.startswith(tuple(prefix)):
        return  # check for bots and user commands
    msg = prefix_filter(prefix=prefix, msg=ctx.content)
    args = ''

    for cmd_name in cmd_list:  # check for every cmd
        cmd_curr = eval(cmd_name + '_curr')
        cmd_alias_list = cmd_aliases_proceed(cmd_curr.aliases)  # create aliases for all the commands

        if not msg.startswith(tuple(cmd_trigger_on(cmd_name, cmd_alias_list))):
            continue  # check if msg starts with cmd name or its alias

        if msg.find(' ') > 0:  # check if there are any args in msg
            args = str(msg[msg.find(' ') + 1:])
        _cmd_exec_type = cmd_curr.cmd_type

        if cmd_curr.group in cmd_args_exception or cmd_curr.group == 'special' and len(args) == 0:
            cmd_out = cmd_curr.func(bot_prefix=prefix)  # check for args
        else:
            if len(args) < 1:  # check if cmd should be exec w/ args
                cmd_out, _cmd_exec_type = cmd_args_not_found(cmd_name, cmd_curr.cmd_missarg_group), None
            else:
                cmd_out = cmd_curr.func(str(args), prefix)

        if _cmd_exec_type == 'embed':  # embed check
            await ctx.channel.send(embed=cmd_out)
        elif _cmd_exec_type == 'button':  # buttons check
            await ctx.channel.send(view=cmd_out)
        else:  # regular message
            await ctx.channel.send(cmd_out)


bot.run(TOKEN)
