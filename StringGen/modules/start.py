from pyrogram import filters
from pyrogram.types import Message

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cdbf07e687a7de3ef012e.jpg",
        caption=f"""𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂\n╮⦿ مرحباً بك عزيزي : {message.from_user.first_name},\n╯⦿  اسمي : {Anony.mention},\n╮⦿ تم صنعي من قبل فيجا\n╯⦿ اعمل علي استخراج جلسات""",
        reply_markup=keyboard,
    )
    await add_served_user(message.from_user.id)



