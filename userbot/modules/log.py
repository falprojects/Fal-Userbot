# credits: mrconfused
# Recode by @mrismanaziz
# t.me/SharingUserbot

import asyncio

from telethon import events

from userbot import BOTLOG_CHATID, CMD_HANDLER as cmd
from userbot import CMD_HELP, LOGS, bot
from userbot.modules.sql_helper import no_log_pms_sql
from userbot.modules.sql_helper.globals import addgvar, gvarstatus
from userbot.modules.vcg import vcmention
from userbot.utils import _format, edit_delete, edit_or_reply
from userbot.utils.tools import media_type

from userbot.utils import fal_cmd


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@bot.on(events.ChatAction)
async def logaddjoin(fal):
    user = await fal.get_user()
    chat = await fal.get_chat()
    if not (user and user.is_self):
        return
    if hasattr(chat, "username") and chat.username:
        chat = f"[{chat.title}](https://t.me/{chat.username}/{fal.action_message.id})"
    else:
        chat = f"[{chat.title}](https://t.me/c/{chat.id}/{fal.action_message.id})"
    if fal.user_added:
        tmp = fal.added_by
        text = f"u📩 **#TAMBAH_LOG\n •** {vcmention(tmp)} **Menambahkan** {vcmention(user)}\n **• Ke Grup** {chat}"
    elif fal.user_joined:
        text = f"📨 **#LOG_GABUNG\n •** [{user.first_name}](tg://user?id={user.id}) **Bergabung\n • Ke Grup** {chat}"
    else:
        return
    await fal.client.send_message(BOTLOG_CHATID, text)


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
@bot.on(events.MessageEdited(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(fal):
    if BOTLOG_CHATID == -100:
        return
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        return
    sender = await fal.get_sender()
    await asyncio.sleep(0.5)
    if not sender.bot:
        chat = await fal.get_chat()
        if not no_log_pms_sql.is_approved(chat.id) and chat.id != 777000:
            if LOG_CHATS_.RECENT_USER != chat.id:
                LOG_CHATS_.RECENT_USER = chat.id
                if LOG_CHATS_.NEWPM:
                    await LOG_CHATS_.NEWPM.edit(
                        LOG_CHATS_.NEWPM.text.replace(
                            "**💌 #PESAN_BARU**",
                            f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                        )
                    )
                    LOG_CHATS_.COUNT = 0
                LOG_CHATS_.NEWPM = await fal.client.send_message(
                    BOTLOG_CHATID,
                    f"**💌 #MENERUSKAN #PESAN_BARU**\n** • Dari : **{_format.mentionuser(sender.first_name , sender.id)}\n** • User ID:** `{chat.id}`",
                )
            try:
                if fal.message:
                    await fal.client.forward_messages(
                        BOTLOG_CHATID, fal.message, silent=True
                    )
                LOG_CHATS_.COUNT += 1
            except Exception as e:
                LOGS.warn(str(e))


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.mentioned))
@bot.on(events.MessageEdited(incoming=True, func=lambda e: e.mentioned))
async def log_tagged_messages(hmm):
    if BOTLOG_CHATID == -100:
        return
    halal = await hmm.get_chat()

    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        return
    if (
        (no_log_pms_sql.is_approved(halal.id))
        or (BOTLOG_CHATID == -100)
        or (await hmm.get_sender() and (await hmm.get_sender()).bot)
    ):
        return
    full = None
    try:
        full = await hmm.client.get_entity(hmm.message.from_id)
    except Exception as e:
        LOGS.info(str(e))
    messaget = media_type(hmm)
    resalt = f"<b>📨 #TAGS #MESSAGE</b>\n<b> • Dari : </b>{_format.htmlmentionuser(full.first_name , full.id)}"
    if full is not None:
        resalt += f"\n<b> • Grup : </b><code>{halal.title}</code>"
    if messaget is not None:
        resalt += f"\n<b> • Jenis Pesan : </b><code>{messaget}</code>"
    else:
        resalt += f"\n<b> • 👀 </b><a href = 'https://t.me/c/{halal.id}/{hmm.message.id}'>Lihat Pesan</a>"
    resalt += f"\n<b> • Message : </b>{hmm.message.message}"
    await asyncio.sleep(0.5)
    if not hmm.is_private:
        await hmm.client.send_message(
            BOTLOG_CHATID,
            resalt,
            parse_mode="html",
            link_preview=False,
        )


@fal_cmd(pattern="save(?: |$)(.*)")
async def log(log_text):
    if BOTLOG_CHATID:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"**#LOG / Chat ID:** {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(BOTLOG_CHATID, textx)
        else:
            await edit_delete(log_text, "**Apa yang harus saya simpan?**")
            return
        await edit_delete(log_text, "**Berhasil disimpan di Grup Log**")
    else:
        await edit_delete(
            log_text,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )


@fal_cmd(pattern="log$")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.disapprove(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Diaktifkan**", 15
            )


@fal_cmd(pattern="nolog$")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.approve(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Dimatikan**", 15
            )


@fal_cmd(pattern="pmlog (on|off)$")
async def set_pmlog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await edit_or_reply(event, "**PM LOG Sudah Diaktifkan**")
        else:
            addgvar("PMLOG", h_type)
            await edit_or_reply(event, "**PM LOG Berhasil Dimatikan**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await edit_or_reply(event, "**PM LOG Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**PM LOG Sudah Dimatikan**")


@fal_cmd(pattern="gruplog (on|off)$")
async def set_gruplog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await edit_or_reply(event, "**Group Log Sudah Diaktifkan**")
        else:
            addgvar("GRUPLOG", h_type)
            await edit_or_reply(event, "**Group Log Berhasil Dimatikan**")
    elif h_type:
        addgvar("GRUPLOG", h_type)
        await edit_or_reply(event, "**Group Log Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**Group Log Sudah Dimatikan**")


CMD_HELP.update(
    {
        "log": f"**Modules : **`log`\
        \n\n •  **Command  :** `{cmd}save`\
        \n  •  **Function  : **Untuk Menyimpan pesan yang ditandai ke grup pribadi.\
        \n\n •  **Command  :** `{cmd}log`\
        \n  •  **Function  : **Untuk mengaktifkan Log Chat dari obrolan/grup itu.\
        \n\n •  **Command  :** `{cmd}nolog`\
        \n  •  **Function  : **Untuk menonaktifkan Log Chat dari obrolan/grup itu.\
        \n\n •  **Command  :** `{cmd}pmlog on/off`\
        \n  •  **Function  : **Untuk mengaktifkan atau menonaktifkan pencatatan pesan pribadi\
        \n\n •  **Command  :** `{cmd}gruplog on/off`\
        \n  •  **Function  : **Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup pmlogger."
    }
)
