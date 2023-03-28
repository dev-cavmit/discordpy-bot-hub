from random import choice as rand_ch
from media.fun_media import vid_help
from modules.commands_assist.pre_config import *
from modules.commands_assist.proceed import *

display_name = 'Commands Help List'
aliases = ['halp', 'what_is', '?', '/']
group = 'special'
cmd_missarg_group = '<command to get info about or leave unfilled for general info>'
cmd_type = 'embed'
color = embed_color

for _cmd in cmd_list:  # importing all the cmds variables
    globals()[_cmd + '_curr_folder'] = (cmd_folder_dot + _cmd)
    globals()[_cmd + '_curr'] = import_module(eval(_cmd + '_curr_folder'))


def func(args='1', bot_prefix=None):
    help_footer = f"Type {rand_ch(bot_prefix)}help <command> for more command info"
    cmd_found = None
    cmds_per_page = 9
    pages_count = (len(cmd_list) // cmds_per_page) + 1
    page_containment = []
    cmd_description_pair = {}

    aliases.append('help')  # check for double-triggered help
    if args.startswith(tuple(aliases)) and not args.isnumeric():
        return discord.Embed(description=f'Help!\n{rand_ch(vid_help)}', color=color)
    aliases.remove('help')

    out = discord.Embed(title=display_name, color=color)  # embed starts

    for _cmd in cmd_list:  # generate cmd-description pair
        _cmd_curr = eval(_cmd + '_curr')
        _show_example_groups = ['text']  # add description
        _description = f"**{_cmd_curr.display_name}**"
        if _cmd == "help":
            _description += "\n*You're here!*"
        if _cmd_curr.group in _show_example_groups:
            _description += f"\n{_cmd_curr.func('Text Example')}"
        cmd_description_pair[_cmd] = _description

    for _cmd in cmd_list:  # make a total list of all the cmds
        _cmd_curr = eval(_cmd + '_curr')
        alias_list = _cmd_curr.aliases  # cmd_aliases_proceed(_cmd_curr.aliases)  # TODO: aliases as used for cmds

        _trigger = alias_list  # check if cmd after help
        _trigger.append(_cmd)
        if args in _trigger:
            cmd_found = _cmd

        if _cmd == 'help' and args.isnumeric() and 0 < int(args) <= pages_count:
            for _page in range(pages_count):  # prepare pages' containment
                _search_from = _page * cmds_per_page
                _search_end = (_page + 1) * cmds_per_page
                if _search_end > len(cmd_list):
                    _search_end -= (cmds_per_page - len(cmd_list) % cmds_per_page)
                page_containment.append(cmd_list[_search_from:_search_end])

            for _cmd_on_page in page_containment[int(args)-1]:
                out.add_field(name=_cmd_on_page, value=cmd_description_pair[_cmd_on_page])
            help_footer += f"\nHelp page {args} of {pages_count}"

    if cmd_found:
        out.clear_fields()
        _cmd = eval(cmd_found + '_curr')
        _description = f"**{cmd_found}** command\nAliases: {' '.join([f'`{alias}`' for alias in _cmd.aliases])}\n" \
                       f"Usage: {rand_ch(bot_prefix)}{cmd_found} {_cmd.cmd_missarg_group}"
        out.add_field(name=_cmd.display_name, value=_description)
    elif args and not cmd_found and not args.isnumeric():
        out.clear_fields()
        out.add_field(name=f'Command {args} not found',
                      value='Please search for the command in the main list by typing in\n`'
                            f'{rand_ch(bot_prefix)}help` and try again', inline=False)

    out.set_footer(text=help_footer)

    return out
