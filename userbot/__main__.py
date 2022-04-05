# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module


from userbot import (
    BOT_TOKEN,
    BOT_USERNAME,
    BOT_VER,
    BOTLOG_CHATID,
    ALIVE_LOGO,
    LOGS,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot
from userbot.utils.tools import bacot_kontol

try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    user = bot.get_me()
    LOGS.info(f"✨Fal-Userbot✨ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def userbot_on():
    user = await bot.get_me()
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(
                BOTLOG_CHATID, ALIVE_LOGO, caption=f"** Fal-Userbot Berhasil Diaktifkan✨**\n━━━━━━━━━━━━━━━━━━━\n✦ **Oᴡɴᴇʀ Bᴏᴛ :** [{user.first_name}](tg://user?id={user.id})\n✦ **Bᴏᴛ Vᴇʀ :** `8.2`\n━━━━━━━━━━━━━━━━━━━\n✦ **Owner​ :** @falprojects\n✦ **Channel​ :** @fallprojects \n━━━━━━━━━━━━━━━━━━━"
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "Vars BOT_TOKEN tidak terdeteksi, mari bikin bot di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
