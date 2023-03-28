# TODO IDEA: Making this thing automatically be triggered on text group commands
name = 'Text Generator'
group = 'text'
aliases = ['small_caps', 'caps']

alph_def = """abcdefjhigklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
alph_smallcaps = """ᴀʙᴄᴅᴇғᴊʜɪɢᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢABCDEFJHIGKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
alph_bubbles = """ⓐⓑⓒⓓⓔⓕⓙⓗⓘⓖⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒿⒽⒾⒼⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ①②③④⑤⑥⑦⑧⑨0`~!@#$%^&⊛()⊖_=+[{]}\|;:'",<.>/?"""
alph_bold = """𝐚𝐛𝐜𝐝𝐞𝐟𝐣𝐡𝐢𝐠𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐉𝐇𝐈𝐆𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
alph_backwards = """﹖/>.<,"'﹕﹔|\}]{[+=⁻⁻)(*&^﹪﹩#@﹗~`098765432߁ZYXWVUTꙄᴙpꟼOᴎM⅃KGIHJꟻƎbↃdAzγxwvUɟƨᴙpqoᴎmlkgi⑁jʇɘbↄdɒ"""
alph_upsidedown = """¿/>.<,"':;|\{[}]+=⁻-()*⅋^﹪﹩#@¡~`0987654321zʎxʍ��ʇsɹbdouɯןʞƃıɥɾɟǝpɔqɐzʎxʍʌnʇsɹbdouɯןʞƃıɥɾɟǝpɔqɐ"""

def func(args):

    out = ""

    for ch in args:
        if ch in alph_def:
            out += alph_smallcaps[alph_def.index(ch)]
        else:
            out += ch

    return out
