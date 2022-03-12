from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

# главная клавиатура
markup_main = ReplyKeyboardMarkup(resize_keyboard=True)
menu_buttons = KeyboardButton('Меню с кнопками')
menu_nobuttons = KeyboardButton('Меню без кнопок')

markup_main.row(menu_buttons, menu_nobuttons)

# клавиатура выбора валют
markup = ReplyKeyboardMarkup(resize_keyboard=True)
item_1 = InlineKeyboardButton(f'EUR')
item_2 = InlineKeyboardButton(f'USD')
item_3 = InlineKeyboardButton(f'JPY')
item_4 = InlineKeyboardButton(f'RUB')
back = InlineKeyboardButton(f'Назад')

markup.row(item_1, item_2, item_3, item_4, back)

# клавиатура назад
markup_back = ReplyKeyboardMarkup(resize_keyboard=True)
back = InlineKeyboardButton(f'Назад')

markup_back.row(back)

