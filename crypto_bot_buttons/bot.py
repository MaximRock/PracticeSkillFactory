import telebot # импорт библиотеки
from extenButtons import MyExceptionButtons, ConvertButtons # импорт классов для меню с кнопками
from extensions import MYException, MYConverter # импорт классов для меню без кнопок
from config import keys, TOKEN # импорт словаря валют и TOKENа
import markup as nav # импорт клавиатуры

bot = telebot.TeleBot(TOKEN)

# начальное приветствие, комманды 'start', 'help'
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = '''Привет! \n Я бот для конвертации валют.
Для начала работы выберите <Меню> которое тебе удобно.
Мои команды:
/start - начало работы,
/help - помощь,
/values - список валют.'''

    bot.reply_to(message, text, reply_markup=nav.markup_main) # клавиатура
    msg = bot.send_message(message.chat.id, 'Выберите Меню')
    bot.register_next_step_handler(msg, currency_buttons)

# список доступных валют
@bot.message_handler(commands=['values'])
def currency(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)
    msg = bot.send_message(message.chat.id, 'Выберите действие')
    bot.register_next_step_handler(msg, currency_buttons)

# условие выбора меню
@bot.message_handler(content_types=['text', ])
def currency_buttons(message):
    if message.text == 'Меню без кнопок': # если Меню без кнопок
        currency_menu_back(message)        # то переходим в currency_menu_back
    elif message.text == 'Меню с кнопками': # если Меню с кнопками
        currency_menu_buttons(message)      # то переходим в currency_menu_buttons
    elif message.text == '/values':         # если /values
        currency(message)                   # то переходим в currency

# приветствие меню без кнопок
@bot.message_handler(content_types=['text', ])
def currency_menu_back(message):
    text = '''И так, начнем. 
Введите команды в слелующей последовательности:
<Имя валюты> <В какую валюту перевести> <Количество переводимой валюты>.
Для возврата выбери <Назад>'''
    bot.reply_to(message, text, )
    msg = bot.send_message(message.chat.id, 'Введите валюту', reply_markup=nav.markup_back) # клавиатура
    bot.register_next_step_handler(msg, currency_choice)

# обработка кнопки назад
@bot.message_handler(content_types=['text', ])
def currency_choice(message):
    if message.text == 'Назад':
        start(message)
    elif message.text != 'Назад':
        currency_entry(message)

# обрабатываем сообщение пользователя
# <Имя валюты> <В какую валюту перевести> <Количество переводимой валюты>.
@bot.message_handler(content_types=['text', ])
def currency_entry(message):

    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise MYException('Слишком много параметров')
        elif len(values) < 3:
            raise MYException('Слишком мало параметров')

        quote, base, amount = values
        total_base = MYConverter.get_price(quote, base, amount) # класс, метод ()

    except MYException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
        msg = bot.send_message(message.chat.id, 'Внимательно вводите данные')
        bot.register_next_step_handler(msg, currency_entry)
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

        text = '''
Если хотите продолжить введите валюту.
Если надоело выберите <Назад>.'''
        msg = bot.send_message(message.chat.id, text, )
        bot.register_next_step_handler(msg, currency_choice)

# меню валют с кнопками
@bot.message_handler(content_types=['text', ])
def currency_menu_buttons(message):
    text = '''Выберите предложенную валюту в следующей последовательности:
<Имя валюты> <В какую валюту перевести> <Количество переводимой валюты>.
Для возврата выберите - <Назад>.'''
    bot.reply_to(message, text)
    msg = bot.send_message(message.chat.id, 'Выбери валюту >', reply_markup=nav.markup) # клавиатура
    bot.register_next_step_handler(msg, menu_buttons)

# обработка кнопки назад
@bot.message_handler(content_types=['text', ])
def menu_buttons(message):
    if message.text == 'Назад':
        start(message)
    elif message.text != 'Назад':
        currency_quote(message)

# обработка первой валюты
@bot.message_handler(content_types=['text', ])
def currency_quote(message):

    try:
        quote = message.text
        bot.reply_to(message, f'Ваша валюта - "{quote}"')

        ConvertButtons.get_quote(quote) # класс, метод()

        msg = bot.send_message(message.chat.id, 'Выбери валюту для перевода')
        bot.register_next_step_handler(msg, currency_base, quote)

    except MyExceptionButtons as a:
        bot.reply_to(message, f'Ошибка пользователя - \n{a}')
        msg = bot.send_message(message.chat.id, 'Выбери валюту из списка')
        bot.register_next_step_handler(msg, menu_buttons)
    except Exception as a:
        bot.reply_to(message, f'Не удалось обработать команду.\n{a}')


    # if quote in keys.values():
    #     bot.reply_to(message, f'Ваша валюта - "{quote}"')
    #     msg = bot.send_message(message.chat.id, 'Выбери валюту для перевода')
    #     bot.register_next_step_handler(msg, currency_base, quote)
    # else:
    #     bot.reply_to(message, f'Будь внимательней при выборе')
    #     msg = bot.send_message(message.chat.id, 'Выбери валюту из списка')
    #     bot.register_next_step_handler(msg, menu_buttons)

# обработка второй валюты
@bot.message_handler(content_types=['text', ])
def currency_base(message, quote: str):

    try:
        base = message.text
        bot.reply_to(message, f'Ваша валюта - {base}')

        ConvertButtons.get_base(quote, base) # класс, метод()

        msg = bot.send_message(message.chat.id, 'Введите количество')
        bot.register_next_step_handler(msg, currency_amount, quote, base)

    except MyExceptionButtons as a:
        bot.reply_to(message, f'Ошибка пользователя - \n{a}')
        msg = bot.send_message(message.chat.id, 'Выбери валюту для перевода')
        bot.register_next_step_handler(msg, currency_base, quote)
    except Exception as a:
        bot.reply_to(message, f'Не удалось обработать команду.\n{a}')

    # base = message.text
    # if (base in keys.values()) and (quote != base):
    #     bot.reply_to(message, f'Ваша валюта - {base}')
    #     msg = bot.send_message(message.chat.id, 'Введите количество')
    #     bot.register_next_step_handler(msg, currency_amount, quote, base)
    # else:
    #     bot.reply_to(message, f'Введите валюту из списка')
    #     msg = bot.send_message(message.chat.id, 'Выбери валюту для перевода')
    #     bot.register_next_step_handler(msg, currency_base, quote)

# обработка количества валюты и суммы валюты
@bot.message_handler(content_types=['text', ])
def currency_amount(message, quote, base):
    # amount = message.text
    # bot.reply_to(message, f'Введенное количество - {amount}')

    try:
        amount = message.text
        bot.reply_to(message, f'Введенное количество - {amount}')

        total = ConvertButtons.get_total(quote, base, amount)  # класс, метод()

        text = f'Цена {amount} {quote} в {base} - {total}'
        bot.send_message(message.chat.id, text)

        text = '''
Если хотите продолжить введите валюту.
Если надоело выберите <Назад>.'''
        msg = bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(msg, back)

    except MyExceptionButtons as a:
        bot.reply_to(message, f'Ошибка пользователя - \n{a}')
        msg = bot.send_message(message.chat.id, 'Введите колличество валюты')
        bot.register_next_step_handler(msg, currency_amount, quote, base)
    except Exception as a:
        bot.reply_to(message, f'Не удалось обработать команду.\n{a}')

#     try:
#         amount = float(amount)
#         if amount > 0:
#             total = ConvertButtons.get_total(quote, base, amount) # класс, метод ()
#
#             text = f'Цена {amount} {quote} в {base} - {total}'
#             bot.send_message(message.chat.id, text)
#
#             text = '''
# Если хотите продолжить введите валюту.
# Если надоело выберите <Назад>.'''
#             msg = bot.send_message(message.chat.id, text)
#             bot.register_next_step_handler(msg, back)
#         else:
#             bot.reply_to(message, f'Введено не верное колличество валюты')
#             msg = bot.send_message(message.chat.id, 'Введите колличество валюты')
#             bot.register_next_step_handler(msg, currency_amount, quote, base)
#
#     except ValueError:
#         bot.reply_to(message, f'Введено не верное колличество валюты')
#         msg = bot.send_message(message.chat.id, 'Введите колличество валюты')
#         bot.register_next_step_handler(msg, currency_amount, quote, base)
#
#     except TypeError:
#         bot.reply_to(message, f'Введено не верное колличество валюты')
#         msg = bot.send_message(message.chat.id, 'Введите колличество валюты')
#         bot.register_next_step_handler(msg, currency_amount, quote, base)

@bot.message_handler(content_types=['text', ]) # обработка кнопки назад

def back(message):
    if message.text == 'Назад':
        start(message)
    elif message.text != 'Назад':
        currency_quote(message)

bot.polling(none_stop=True)