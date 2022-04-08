""" Userbot module for other small commands. """
from userbot import CMD_HELP, owner, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, fal_cmd


@fal_cmd(pattern="ihelp$")
async def usit(e):
    await edit_or_reply(e,
                        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
                        f"❆ **Channel Fal :** [N](t.me/fallprojects)\n"
                        f"❆ **Owner Repo :** [N](t.me/falprojects)\n"
                        f"❆ **Repo :** [Fal-Userbot](https://github.com/falprojects/Fal-Userbot)\n",
                        )


@fal_cmd(pattern="vars$")
async def var(m):
    await edit_or_reply(m,
                        f"**Disini Daftar Vars Dari {owner}:**\n"
                        "\n[DAFTAR VARS](https://raw.githubusercontent.com/falprojects/Fal-Userbot/Fal-Userbot/varshelper.txt)",
                        )


CMD_HELP.update({
    "helper":
    f"`{cmd}ihelp`\
\nUsage: Bantuan Untuk Fal-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
