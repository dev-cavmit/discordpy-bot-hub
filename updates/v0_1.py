from datetime import datetime
upd_timestamp_utc3 = 1672354450
upd_timestamp_utc = upd_timestamp_utc3 - 3600 * 3
upd_timestamp = datetime.fromtimestamp(upd_timestamp_utc)
upd_en = upd_timestamp.strftime("%m/%d/%Y")
upd_eu = upd_timestamp.strftime("%d.%m.%Y")

upd_name = 'Help Update'
upd_version = '0.1'
upd_release_date = f'{upd_en} ({upd_eu}) UTC'
upd_author = "cavmit (<@1055186314712076288>)"
upd_idea = "RandomBirdy (<@200867095666229248>)"
upd_notes = f"""
First noted update since 27.11.2022
Features:
- Added **updates** command with featured changes included
- Added **about** command that describes about the bot and an author
- Rebuilt **help** command that shows brief and all the information about the commands exists
Now dynamically splits for pages, set to 9 elements per page by default
- Improved performance
- **ping** command now sends button

Our team wish you a Happy New Year!
Good luck, lil' rolls"""
