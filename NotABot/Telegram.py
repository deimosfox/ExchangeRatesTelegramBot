import telebot;
from NotABot import MessageParser
from NotABot import Logger

bot = telebot.TeleBot('1091007509:AAFJA5jX2it5EsFebiLfeC9EIoMLS3mELGQ');

Logger.log.info("BOT START")


@bot.message_handler(
    content_types=["text", "sticker", "pinned_message", "photo", "audio", "document", "video", "video_note", "voice",
                   "location", "contact"])
def get_text_messages(message):
    if message.chat.type == 'private':
        if message.content_type == 'text':
            if message.text == "Привет":
                bot.send_message(message.from_user.id,
                                 "Привет, я пока тупой , но скоро стану самым лучшим ботом , честно-честно")
            elif message.text == "/help":
                Logger.log.info("Help data was sent to user")
                bot.send_message(message.from_user.id, "Бот имеет 2 функции:")
                bot.send_message(message.from_user.id, "1) Выводить банки и курсы , указанного вами региона")
                bot.send_message(message.from_user.id, "2) Выводить курс валюты по Цб на конкретную дату")
                bot.send_message(message.from_user.id, "На данный момент обслуживаются 5 валют:USD,EUR,GBP,JPY,CNY")
                bot.send_message(message.from_user.id, "Бот работает только по 29 городам РФ")
                bot.send_message(message.from_user.id, "Статистика берется с сайта banki.ru")
                bot.send_message(message.from_user.id,
                                 "Строка подается в произвольном формате , но должна встречать в себе упоминания валют/городов")
                bot.send_message(message.from_user.id,
                                 "Для поиска по дате , используйте ключевые слова:  \n1)цб\n2)центробанк \n дата подается в формате дд.мм.гггг")
            else:
                key, tmp, msg = MessageParser.ParsMessage(message.text)
                if key == 1:
                    if tmp == 1:
                        bot.send_message(message.from_user.id,
                                         "неверно указана валюта и регион , введите /help для описания функционала")
                    elif tmp == 2:
                        bot.send_message(message.from_user.id, "данную валюту не обслуживают в выбраном регионе")
                    elif tmp == 3:
                        bot.send_message(message.from_user.id,
                                         "валюта не указана или не поддерживается ботом , введите /help для описания функционала")
                    elif tmp == 4:
                        bot.send_message(message.from_user.id,
                                         "город не указан или не поддерживается ботом , введите /help для описания функционала")
                    elif msg != 0:
                        Logger.log.info("Bot given an info about current into region")
                        bot.send_message(message.from_user.id, msg)
                        for i in range(min(5, len(tmp))):
                            bot.send_message(message.from_user.id, "Банк: " + tmp[i][0])
                            bot.send_message(message.from_user.id, "Покупка: " + tmp[i][1])
                            bot.send_message(message.from_user.id, "Продажа: " + tmp[i][2])
                if key == 2:
                    if tmp == 2:
                        bot.send_message(message.from_user.id, "Данные по выбраной валюте на данную дату не найдены")
                    else:
                        Logger.log.info("Bot given an info about current at date")
                        bot.send_message(message.from_user.id, msg)
                        bot.send_message(message.from_user.id, tmp + "руб")

        elif message.content_type == 'sticker':
            bot.send_message(message.from_user.id, "классный стикер!!! я люблю стикеры...и деньги *_*")
        else:
            bot.send_message(message.from_user.id, "извини, я не понимаю тебя")

    if message.chat.type == 'group':
        if message.content_type == 'text':

            if message.text == "/help":
                bot.send_message(message.chat.id, "Бот имеет 2 функции:")
                bot.send_message(message.chat.id, "1) Выводить банки и курсы , указанного вами региона")
                bot.send_message(message.chat.id, "2) Выводить курс валюты по Цб на конкретную дату")
                bot.send_message(message.chat.id, "На данный момент обслуживаются 5 валют:USD,EUR,GBP,JPY,CNY")
                bot.send_message(message.chat.id, "Бот работает только по 29 городам РФ")
                bot.send_message(message.chat.id, "Статистика берется с сайта banki.ru")
                bot.send_message(message.chat.id,
                                 "Строка подается в произвольном формате , но должна встречать в себе упоминания валют/городов")
                bot.send_message(message.chat.id,
                                 "Для поиска по дате , используйте ключевые слова:  \n1)цб\n2)центробанк \n дата подается в формате дд.мм.гггг")
            else:
                key, tmp, msg = MessageParser.ParsMessage(message.text)
                if key == 1:
                    if msg != 0 and tmp != 2 and tmp != 1:
                        bot.send_message(message.chat.id, msg)
                        for i in range(min(5, len(tmp))):
                            bot.send_message(message.chat.id, "Банк: " + tmp[i][0])
                            bot.send_message(message.chat.id, "Покупка: " + tmp[i][1])
                            bot.send_message(message.chat.id, "Продажа: " + tmp[i][2])
                if key == 2:
                    if tmp == 2:
                        bot.send_message(message.chat.id, "Данные по выбраной валюте на данную дату не найдены")
                    else:
                        bot.send_message(message.chat.id, msg)
                        bot.send_message(message.chat.id, tmp + "руб")


bot.polling(none_stop=True, interval=0)
