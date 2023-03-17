import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from DevilxRobot.events import register
from DevilxRobot import telethn as borg, OWNER_ID, OWNER_NAME
from DevilxRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/58ab61861cf8d5638e801.jpg"
file2 = "https://telegra.ph/file/8ba762344670dfe6b532b.jpg"
file3 = "https://telegra.ph/file/3378e076435eb708f4a1f.jpg"
file4 = "https://telegra.ph/file/58ab61861cf8d5638e801.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    DevilxRobot = f"┗ **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm DevilxRobot**\n"
    DevilxRobot += f"┗ **My Uptime** - `{uptime}`\n"
    DevilxRobot += f"┗ **Telethon Version** - `{version.__version__}`\n"
    DevilxRobot += f"┗ **PTB Version** - `{telegram.__version__}`\n"
    DevilxRobot += f"┗ **Pyrogram Version** - `{pyro}`\n"
    DevilxRobot += f"┗ **My Master** - [𓆩𝐒 𝐀 𝐌𓆪™](tg://user?id={OWNER_ID})\n\n"
    DevilxRobot += f"┗ Thanks For Adding Me In {yes.chat.title}"
    BUTTON = [[Button.url("🚑 Support", "https://t.me/Team_Bot_Support"), Button.url("Updates 📢", "https://t.me/Team_Bot_Update")]]
    on = await borg.send_file(yes.chat_id, file="https://telegra.ph/file/58ab61861cf8d5638e801.jpg",caption=DevilxRobot, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Asuka = f"**┗ Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("GitHub", "https://github.com/Official-Afk-xD/DevilxRobot"), Button.url("Developer ❔", "https://t.me/piro_x_power")]]
    await borg.send_file(event.chat_id, file="https://telegra.ph/file/58ab61861cf8d5638e801.jpg", caption=DevilxRobot, buttons=BUTTON)
