from io import BytesIO

from aiogram import Router, F
from aiogram.types import Message, BufferedInputFile

from src.utils import create_image

router = Router()


@router.message(F.photo)
async def command_likvidirovat(message: Message) -> None:
    await message.answer('Ликвидирую..')
    image = BytesIO()

    try:
        await message.bot.download(message.photo[-1], destination=image)
        await message.reply_photo(photo=BufferedInputFile(create_image.likvidirovat(image.read()),
                                                          filename='likvidirovano.png'))
    except Exception:
        await message.reply('Там ошибка произошла в момент когда я качал или отправлял,'
                            'поэтому сожми его или я хз что еще сделать....')


@router.message()
async def invalid_command(message: Message) -> None:
    await message.reply('Смотри, тебе надо прсто отправить картинку. Я в тебя верю.')
