import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("🍿 Фильм")
    button2 = types.KeyboardButton("🎥 Сериал")

    markup.add(button1, button2)

    bot.send_message(message.chat.id,
    "\n💬 ВЫБЕРИ ФИЛЬМ/СЕРИАЛ ".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def recommendation(message):
    if message.text == "🍿 Фильм":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("💥 Боевик")
        button2 = types.KeyboardButton("👻 Хоррор")
        button3 = types.KeyboardButton("🧑‍🤝‍🧑 Комедия")
        button4 = types.KeyboardButton("👩‍❤️‍👨 Мелодрама")
        button5 = types.KeyboardButton("🌍 Приключения")
        button6 = types.KeyboardButton("👮 Детектив")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, "Отлично! Давай теперь определимся с жанром🤔", reply_markup=markup)

    elif message.text == "🎥 Сериал":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("💢 Боевик")
        button2 = types.KeyboardButton("🧟‍♀️ Хоррор")
        button3 = types.KeyboardButton("🤷‍♀️ Комедия")
        button4 = types.KeyboardButton("👀 Мелодрама")
        button5 = types.KeyboardButton("👩‍🚀 Приключения")
        button6 = types.KeyboardButton("👣 Детектив")
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, "Отлично! Давай теперь определимся с жанром🤔", reply_markup=markup)

    if message.text == "💥 Боевик":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Боевик': \n\n🎞 Мстители\n🎞 Джон Уик\n🎞 Матрица\n🎞 Темный рыцарь\n🎞 Безумный Макс: Дорога ярости")
        welcome(message)
    elif message.text == "👻 Хоррор":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Хоррор': \n\n🎞 Оно\n🎞 Пила\n🎞 Заклятие\n🎞 Астрал\n🎞 Тихое место")
        welcome(message)
    elif message.text == "🧑‍🤝‍🧑 Комедия":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Комедия':\n\n🎞 В джазе только девушки\n🎞 Мальчишник в Вегасе\n🎞 Джентльмены\n🎞 Мальчишник 2\n🎞 Криминальное чтиво")
        welcome(message)
    elif message.text == "👩‍❤️‍👨 Мелодрама":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Мелодрама':\n\n🎞 Титаник\n🎞 Запах женщины\n🎞 Невеста напрокат\n🎞 Быть или не быть")
        welcome(message)
    elif message.text == "🌍 Приключения":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Приключения':\n\n🎞 Пираты Карибского моря\n🎞 Хоббит: Нежданное путешествие\n🎞 Пещера\n🎞 Индиана Джонс и последний крестовый поход\n🎞 Хранители")
        welcome(message)
    elif message.text == "👮 Детектив":
        bot.send_message(message.chat.id, "Рекомендуемые фильмы жанра 'Детектив':\n\n🎞 Семь\n🎞 Загадочная история Бенджамина Баттона\n🎞 Шерлок Холмс\n🎞 В джазе только девушки")
        welcome(message)

    elif message.text == "💢 Боевик":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Боевик': \n\n🎞 Викинги\n🎞 Острые козырьки\n🎞 Бумажный дом\n🎞 Спецназ\n🎞 Твин Пикс")
        welcome(message)
    elif message.text == "🧟‍♀️ Хоррор":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Хоррор': \n\n🎞 Ходячие мертвецы\n🎞 Стрела\n🎞 Декстер\n🎞 Американская история ужасов\n🎞 Секретные материалы")
        welcome(message)
    elif message.text == "🤷‍♀️ Комедия":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Комедия':\n\n🎞 Друзья\n🎞 Симпсоны\n🎞 Во все тяжкие\n🎞 Большой взрыв\n🎞 Парки и зоны отдыха")
        welcome(message)
    elif message.text == "👀 Мелодрама":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Мелодрама':\n\n🎞 Дневники вампира\n🎞 Реальные пацаны\n🎞 Милые обманщицы\n🎞 Побег\n🎞 Революция ")
        welcome(message)
    elif message.text == "👩‍🚀 Приключения":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Приключения':\n\n🎞 Игра престолов\n🎞 Жизнь посторонних\n🎞 Флэш\n🎞 Ганнибал\n🎞 Восьмидесятые")
        welcome(message)
    elif message.text == "👣 Детектив":
        bot.send_message(message.chat.id, "Рекомендуемые сериалы жанра 'Детектив':\n\n🎞 Шерлок\n🎞 Декстер\n🎞 Менталист\n🎞 Кастл\n🎞 Тюдоры")
        welcome(message)


bot.polling(none_stop=True)
