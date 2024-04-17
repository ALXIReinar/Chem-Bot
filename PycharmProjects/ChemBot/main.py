import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F
from aiogram.types import Message
import chem_path


dp = Dispatcher()
TOKEN = 'WRITE YOUR BOT-TOKEN'
bot = Bot(TOKEN)

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'Привет!\nЯ знаю строение и электронную формулу атомов элементов. Поэтому не стесняйся спрашивать их у меня')
    await message.answer('Просто напиши желаемый элемент)')
    await message.answer_photo(chem_path.example, caption='Пример использования:')

@dp.message(F.text.lower() == 'na')
async def na(message: Message):
    await message.answer_photo(chem_path.Na)

@dp.message(F.text.lower() == 'li')
async def li(message: Message):
    await message.answer_photo(chem_path.Li)

@dp.message(F.text.strip().lower() == 'h')
async def h(message: Message):
    await message.answer_photo(chem_path.H2)
    await message.answer_photo(chem_path.H1)

@dp.message(F.text.strip().lower() == 'b')
async def b(message: Message):
     await message.answer_photo(chem_path.B)

@dp.message(F.text.strip().lower() == 'be')
async def be(message: Message):
     await message.answer_photo(chem_path.Be)

@dp.message(F.text.strip().lower() == 'c')
async def c(message: Message):
     await message.answer_photo(chem_path.C)

@dp.message(F.text.strip().lower() == 'n')
async def n(message: Message):
     await message.answer_photo(chem_path.N)

@dp.message(F.text.strip().lower() == 'o')
async def o(message: Message):
     await message.answer_photo(chem_path.O)

@dp.message(F.text.strip().lower() == 'f')
async def f(message: Message):
     await message.answer_photo(chem_path.F)

@dp.message(F.text.strip().lower() == 'ne' )
async def ne(message: Message):
     await message.answer_photo(chem_path.Ne)

@dp.message(F.text.strip().lower() == 'he')
async def he(message: Message):
     await message.answer_photo(chem_path.He)

@dp.message(F.text.strip().lower() == 'mg')
async def mg(message: Message):
     await message.answer_photo(chem_path.Mg)

@dp.message(F.text.strip().lower() == 'al')
async def al(message: Message):
     await message.answer_photo(chem_path.Al)


@dp.message(F.text.strip().lower() == 'si')
async def si(message: Message):
    await message.answer_photo(chem_path.Si)


@dp.message(F.text.strip().lower() == 's')
async def s(message: Message):
    await message.answer_photo(chem_path.S)


@dp.message(F.text.strip().lower() == 'cl')
async def cl(message: Message):
    await message.answer_photo(chem_path.Cl)


@dp.message(F.text.strip().lower() == 'ar')
async def ar(message: Message):
    await message.answer_photo(chem_path.Ar)

@dp.message(F.text.strip().lower() == 'k')
async def k(message: Message):
    await message.answer_photo(chem_path.K)

@dp.message(F.text.strip().lower() == 'ca')
async def ca(message: Message):
     await message.answer_photo(chem_path.Ca)

@dp.message(F.text.strip().lower() == 'sc')
async def sc(message: Message):
     await message.answer_photo(chem_path.Sc)

@dp.message(F.text.strip().lower() == 'ti')
async def ti(message: Message):
     await message.answer_photo(chem_path.Ti)

@dp.message(F.text.strip().lower() == 'v')
async def v(message: Message):
     await message.answer_photo(chem_path.V)

@dp.message(F.text.strip().lower() == 'cr')
async def cr(message: Message):
     await message.answer_photo(chem_path.Cr)

@dp.message(F.text.strip().lower() == 'mn')
async def mn(message: Message):
     await message.answer_photo(chem_path.Mn)

@dp.message(F.text.strip().lower() == 'fe')
async def fe(message: Message):
     await message.answer_photo(chem_path.Fe)

@dp.message(F.text.strip().lower() == 'co')
async def co(message: Message):
     await message.answer_photo(chem_path.Co)

@dp.message(F.text.strip().lower() == 'ni')
async def ni(message: Message):
     await message.answer_photo(chem_path.Ni)

@dp.message(F.text.strip().lower() == 'cu')
async def cu(message: Message):
     await message.answer_photo(chem_path.Cu)

@dp.message(F.text.strip().lower() == 'zn')
async def zn(message: Message):
     await message.answer_photo(chem_path.Zn)

@dp.message(F.text.strip().lower() == 'ga')
async def ga(message: Message):
     await message.answer_photo(chem_path.Ga)

@dp.message(F.text.strip().lower() == 'ge')
async def ge(message: Message):
     await message.answer_photo(chem_path.Ge)

@dp.message(F.text.strip().lower() == 'as')
async def As(message: Message):
     await message.answer_photo(chem_path.As)

@dp.message(F.text.strip().lower() == 'se')
async def se(message: Message):
     await message.answer_photo(chem_path.Se)

@dp.message(F.text.strip().lower() == 'br')
async def br(message: Message):
     await message.answer_photo(chem_path.Br)

@dp.message(F.text.strip().lower() == 'kr')
async def kr(message: Message):
     await message.answer_photo(chem_path.Kr)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())