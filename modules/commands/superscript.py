display_name = 'Small Superscript Text Generator'
aliases = ['super_script', 'small_text']
group = 'text'
cmd_missarg_group = '<some text>'
cmd_type = ''


def func(args, bot_prefix=None):
    alph_def = """abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
    alph_superscript = """ᵃᵇᶜᵈᵉᶠʲʰᶦᵍᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴶᴴᴵᴳᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻ¹²³⁴⁵⁶⁷⁸⁹⁰`~ᵎ@#$%^&*⁽⁾⁻_⁼⁺[{]}\|;:'",<.>/ˀ"""
    out = ""

    for ch in args:
        if ch in alph_def:
            out += alph_superscript[alph_def.index(ch)]
        else:
            out += ch

    return out
