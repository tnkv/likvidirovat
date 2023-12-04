from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_likvidirovat(message: Message) -> None:
    await message.answer(text='Привет тебе надо отправить картинку мне, и я для тебя её ликвидирую.\n\n'
                              'by @igor_tnkv | <a href="https://t.me/+fy4_vaZAbJNlODJi">Телеграм канал</a>',
                         disable_web_page_preview=True)
