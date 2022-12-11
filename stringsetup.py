#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """እባክዎ ወደ my.telegram.org
 በመሄድ የርስዎን API ID እና API HASH ያግኙ። 
በመጀመሪያ API DEVELOPMENT TOOL የሚለውን ይንኩ።
  በመቀጠል የሚጠየቁትን በመሙላት አዲስ Application ይፍጠሩ።
"""
)
APP_ID = int(input("በዚህ ቦታ ላይ ከቴሌግራም ያገኙትን APP ID ያስገቡ: "))
API_HASH = input("በዚህ ቦታ ላይ ከቴሌግራም ያገኙትን API HASH ያስገቡ: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
