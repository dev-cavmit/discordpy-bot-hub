display_name = 'Small Subscript Text Generator'
aliases = ['sub_script', 'smoll_text']
group = 'text'
cmd_missarg_group = '<some text>'
cmd_type = ''


def func(args, bot_prefix=None):
    alph_def = """abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
    alph_subscript = """ₐᵦ𝒸𝒹ₑ𝒻ⱼₕᵢ𝓰ₖₗₘₙₒₚᵩᵣₛₜᵤᵥ𝓌ₓᵧ𝓏ₐBCDₑFⱼₕᵢGₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZ₁₂₃₄₅₆₇₈₉₀`~!@#$%^&*₍₎₋_₌₊[{]}\|;:'",<.>/?"""
    out = ""

    for ch in args:
        if ch in alph_def:
            out += alph_subscript[alph_def.index(ch)]
        else:
            out += ch

    return out
