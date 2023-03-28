import discord
from modules.commands_assist.pre_config import embed_color
from random import choice as rand_ch
from default_config.glob import bot_name, conf_file, prefix  # about the bot


display_name = 'About the bot'
aliases = ['who_are_you']
group = 'special'
cmd_missarg_group = '<not required>'
cmd_type = 'embed'

description_field = f"""Bot prefix(-es): `{'`, `'.join(prefix)}`
{conf_file.description}\n
{conf_file.dev_team}"""


def func(args=None, bot_prefix=None):
    out = discord.Embed(title=f"About the Bot", description=rand_ch(conf_file.splash), color=embed_color)
    out.add_field(name=f"**{bot_name} bot**", value=description_field)
    out.set_image(url=rand_ch(conf_file.description_media))
    out.set_footer(text=f"Business email: {conf_file.business_email}")
    return out
