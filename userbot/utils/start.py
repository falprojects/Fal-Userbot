from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/05dba38c6d7d79cea533e.jpg",
                caption="✨ **Fal-Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @falprojects ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/fallprojects"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
