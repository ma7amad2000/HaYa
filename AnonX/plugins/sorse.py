import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝐇𝐀𝐘𝐀 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╮\n★‹ [⌞ 𝐇𝐀𝐘𝐀 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝𝐀](https://t.me/lN_B_Fl)\n★‹ [𝒉𝒂𝒚𝒂 𝒎𝒖𝒔𝒊𝒄ঌ 『 𝒃𝒐𝒕 ⏎ 』](https://t.me/HAYA01BOT)\n★‹ [『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 𝐓𝐍𝐓 ⏎ 』](https://t.me/lV_P_Nl)\n★‹ [فريق حياه للبرمجه](https://t.me/HL_BG)\n╰═★⊷⌯⧼[⌞ 𝐇𝐀𝐘𝐀 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╯\n ⍟ Welcome to source HaYa""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 𝐓𝐍𝐓 ⏎ 』༄►", url=f"https://t.me/lV_P_Nl"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝐇𝐀𝐘𝐀 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️", url=f"https://t.me/lN_B_Fl"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/HAYA01BOT?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



