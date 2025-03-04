import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.enums import ParseMode
from environs import Env
from ai import generate_text

env = Env()
env.read_env()

bot = Bot(token=env('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Hello {message.from_user.full_name}')

@dp.message()
async def generate_text_handler(message: Message) -> None:
    await message.answer(generate_text(message.text))

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())