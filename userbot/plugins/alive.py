"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.**"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**I'm Alive ^.^** \n`BOT Status : ` **☣Hot**\n\n"
                     f"`My peru owner`: {ALIVE_NAME}\n\n"
                     "`HunterGang UserBot Version:` 1.0\n`Python:` **3.7.4**\n"
                     "`Database Status:` **😀ALL OK**\n\n`Always with you, my master!\n`"
                     "**Bot Creator:** [MrSpider](t.me/MrSpider_Genuine)\n\n"
                     "     [Deploy This HunterGang UserBot](https://github.com/SPIDERBHAI/HunterGang)") 
