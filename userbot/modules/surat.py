from time import sleep

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, fal_cmd


@fal_cmd(pattern='alfatihah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    xnxx = await edit_or_reply(typew, "**Surat Al-Fatihah**")
    sleep(1)
    await xnxx.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await xnxx.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await xnxx.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await xnxx.edit("**māliki yaumid-dīn**")
    sleep(1)
    await xnxx.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await xnxx.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await xnxx.edit("**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**")
    sleep(1)
    await xnxx.edit("**Aamiin..**")
# Create by myself

CMD_HELP.update({
    "surat":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}alfatihah`\
    \n↳ : Surat Al-Fatihah."
})
