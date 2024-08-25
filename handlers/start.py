from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Hello, AIOgram 3.x!")


@router.message(Command("help"))
async def help_me(message: Message) -> None:
    await message.answer("Помощь по командам...")