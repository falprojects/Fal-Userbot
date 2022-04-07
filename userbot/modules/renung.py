# ReCode by @falprojects
# FROM Fal-Userbot <https://github.com/falprojects/Fal-Userbot>
# Halal

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, fal_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@fal_cmd(pattern="ortu(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,
                        "**DOA ORANGTUA ADALAH KUNCI KESUKSESAN ANAK**"
                        )


@fal_cmd(pattern="ingat(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,
                        "**INGAT BAHWA ORANG YANG PALING BAHAGIA BUKAN ORANG-ORANG YANG MENDAPATKAN LEBIH BANYAK, TETAPI MEREKA YANG MEMBERI LEBIH!!**"
                        )


@fal_cmd(pattern="sadar(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,
                        "**SADAR AKAN KEKURANGAN LEBIH BAIK DARIPADA BANGGA AKAN KELEBIHAN!!**"
                        )


@fal_cmd(pattern="org(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew,
                        "**ORANG YANG HATINYA BERSIH, MELIHAT ORANG DENGAN KEBAIKAN DAHULU, ORANG YANG HATINYA KOTOR, MELIHAT ORANG DENGAN KEBURUKAN DAHULU.**"
                        )


@fal_cmd(pattern="self(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await edit_or_reply(typew, "**LEBIH BAIK MERASAKAN SULITNYA PENDIDIKAN SEKARANG DARIPADA MERASAKAN PAHITNYA KEBODOHAN, NANTI!!**"
                        )


CMD_HELP.update(
    {
        "renung": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}ortu\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}ingat\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}sadar\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}org\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}self\
        \n↳ : lihat sendiri\
        \n↳ **COBAIN AJA SENDIRI SEMUA!**.\
    "
    }
)
