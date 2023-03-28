display_name = 'Small Caps Generator'
aliases = ['caps', 'tiny_caps']
group = 'text'
cmd_missarg_group = '<some text>'
cmd_type = ''


def func(args, bot_prefix=None):
    alph_def = """abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
    alph_smallcaps = """ᴀʙᴄᴅᴇғᴊʜɪɢᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
    out = ""

    for ch in args:
        if ch in alph_def:
            out += alph_smallcaps[alph_def.index(ch)]
        else:
            out += ch

    return out
