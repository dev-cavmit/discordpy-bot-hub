from modules.commands_assist.proceed import add_button
display_name = 'Ping (Bot Latency Test)'
aliases = ['latency', 'pong', 'test', 'on_line']
group = 'tech'
cmd_missarg_group = '<no arguments required>'
cmd_type = 'button'


def func(args=None, bot_prefix=None):
    out = add_button(text="Ping", edit=":ping_pong: Pong!")
    return out
