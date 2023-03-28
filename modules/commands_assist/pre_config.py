from os import listdir
from os.path import isfile, join
from importlib import import_module

embed_color = 0x2B303A

groups = {'text': 'Text Generators', 'tech': 'Technical', 'special': 'Special'}
cmd_args_exception = ['tech']

cmd_folder = 'modules/commands/'  # dynamic cmds import
cmd_folder_dot = cmd_folder.replace('/', '.')
cmd_list = [f.replace('.py', '') for f in listdir(cmd_folder) if isfile(join(cmd_folder, f))]

for cmd in cmd_list:  # importing all the cmds variables
    globals()[cmd + '_curr'] = import_module(f"{cmd_folder_dot}{cmd}")
