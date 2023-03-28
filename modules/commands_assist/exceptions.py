from default_config.glob import prefix
from random import choice as rand_ch

rand_ch_prefix = rand_ch(prefix)


def cmd_args_not_found(cmd_name, cmd_missarg_group):
    cmd = f'{rand_ch_prefix}{cmd_name}'
    error_msg = f'**{cmd_missarg_group}** is missing for a command **{cmd_name}**.\n' \
                f'Please use the command again: `{cmd} {cmd_missarg_group}`\n' \
                f'or use: `{rand_ch_prefix}help {cmd_name}` to get more info.'
    return error_msg
