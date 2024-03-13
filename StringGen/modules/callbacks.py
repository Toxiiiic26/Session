from pyrogram import filters
from pyrogram.types import CallbackQuery

from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import gen_key
from StringGen.modules.gen import gen_session

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard



@Anony.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂\n╮⦿ هييه ياروع اختار ما تشاء\n╯⦿ من جلسات متطوره",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)




@Anony.on_callback_query(
    filters.regex(pattern=r"^gahhsk$")
)
async def f_staryyyit(_, cq: CallbackQuery):
    await cq.message.reply_text(
            text=f"""𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂\n╮⦿ مرحباً بك عزيزي\n╯⦿ اتبع التعليمات لستخراج الصحيح\n╮⦿ اولا قم بضغط علي : sᴇssɪᴏɴ\n╯⦿ ثانياً: اختار اصدار الذي تريده\n╮⦿ ثالثاً قم بارسال: ᴀᴘɪ ɪᴅ\n╯⦿ رابعاً  قم بارسال: ᴀᴘɪ ʜᴀsʜ\n╮⦿ خامساً قم بارسال رقم الهاتف\n╯⦿ ثم ارسال كود التحقق هكذا 1 2 3 4\n╯⦿ ثم ارسل كلمه المرور\n╮⦿ ثم اذهب للرسال المحفوظه\n╯⦿ وتفقد الجلسه تم استخرجها""",
        reply_markup=keyboard,
    )
    await cq.edit_message_text(e, disable_web_page_preview=True)