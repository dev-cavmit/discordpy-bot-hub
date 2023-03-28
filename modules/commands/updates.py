from random import choice as rand_ch
from os import listdir
from os.path import isfile, join
import importlib
import discord

display_name = 'Changelog of recent updates'
aliases = ['update', 'change_log', 'new']
group = 'special'
cmd_missarg_group = '<version or leave unfilled for the latest update>'
cmd_type = 'embed'
color = 0x2B303A

upd_folder = 'updates/'  # dynamic upd import
upd_folder_dot = upd_folder.replace('/', '.')
upd_list = [f.replace('.py', '') for f in listdir(upd_folder) if isfile(join(upd_folder, f))]
upd_list.reverse()
latest_version = upd_list[0].replace('_', '.')

for upd in upd_list:  # importing all the updates' variables
    globals()[upd + '_curr_folder'] = (upd_folder_dot + upd)
    globals()[upd + '_curr'] = importlib.import_module(eval(upd + '_curr_folder'))

upd_note_header_field, upd_note_field = None, None  # header for the embed


def get_upd_notes(upd_curr):
    global upd_note_header_field, upd_note_field
    upd_note_header_field = f"{upd_curr.upd_name} 「v.{upd_curr.upd_version} | {upd_curr.upd_release_date}」"
    upd_note_field = f"""
    {upd_curr.upd_notes}\n
    Codded by: {upd_curr.upd_author}
    Update Ideas: {upd_curr.upd_idea}
    """
    return upd_note_header_field, upd_note_field


def func(args=None, bot_prefix=None):
    version = args
    if not version:
        version = upd_list[0]
    upd_curr = eval(version + '_curr')
    get_upd_notes(upd_curr)

    out = discord.Embed(title=display_name, color=color)
    out.add_field(name=upd_note_header_field, value=upd_note_field)
    out.set_footer(text=f"Latest Update: {latest_version}\n"
                        f"Type {rand_ch(bot_prefix)}version <version> for more info about exact version release")
    return out

