"""Global default config for all the ongoing bot projects"""
from sys import argv
from importlib import import_module
import discord  # default discord config
intents = discord.Intents.default()
intents.message_content = True

current_file_name = argv[0].split('/')[-1].replace('.py', '')  # current running bot's config file
bot_name = current_file_name.replace('start_', '')
conf_file = import_module(f"default_config.bots.{bot_name}")
prefix = conf_file.prefix
