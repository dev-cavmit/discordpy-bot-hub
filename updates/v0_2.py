from datetime import datetime
upd_timestamp_utc3 = 1680006877
upd_timestamp_utc = upd_timestamp_utc3 - 3600 * 3
upd_timestamp = datetime.fromtimestamp(upd_timestamp_utc)
upd_en = upd_timestamp.strftime("%m/%d/%Y")
upd_eu = upd_timestamp.strftime("%d.%m.%Y")

upd_name = 'Reformatting'
upd_version = '0.2'
upd_release_date = f'{upd_en} ({upd_eu}) UTC'
upd_author = "cavmit (<@1055186314712076288>)"
upd_idea = "RandomBirdy (<@200867095666229248>)"
upd_notes = f"""
Second Update here!
Features:
- Reformatted the entire project code;
- General optimization;
- Now open-source under the MIT License;
- Modular code.

TODOs:
- `help` command reconstruction;
- Aliases logic reconstruction;
- Community server.

Have a good day, with loaf for you"""
