import discord
from discord.ui import Button, View


def prefix_filter(prefix=None, msg=None):  # removes prefix from msg
    for _prefix in prefix:
        msg = msg.replace(_prefix, '', 1)
    return msg


def cmd_aliases_proceed(alias_list):  # modify aliases: first 3 letters of word, add alia without "_", and both combined
    aliases = []
    for a in alias_list:
        aliases.append(a)
        if len(a) > 3:
            aliases.append(a[0:3] + a[a.find('_') + 1:a.find('_') + 4]) if '_' in a else aliases.append(a[0:3])
        if '_' in a:
            aliases.append(a[:a.find('_')])
            aliases.append(a.replace('_', ''))
    return aliases


def cmd_trigger_on(cmd_name, cmd_alias_list):  # create a list of triggering commands and aliases by cmd name
    _a = [cmd_name]
    for alias in cmd_alias_list:
        _a.append(alias)
    return _a


def add_button(text=None, emoji=None, style=None, url=None, edit=None):
    _style_pair = {'green': discord.ButtonStyle.green, 'red': discord.ButtonStyle.danger}
    _view = View()
    _button = Button() if not url else Button(url=url)

    _button.label = text
    if emoji:
        _button.emoji = emoji
    if style:
        _button.style = _style_pair.get(style)

    if edit:
        async def button_callback(interaction):
            await interaction.response.edit_message(content=edit)
        _button.callback = button_callback

    _view.add_item(_button)
    return _view
