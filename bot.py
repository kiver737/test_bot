# import telebot
# import os

# # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
# TOKEN = '7646993468:AAEJ4aRU8g21Ym9fEZ5v1rttGBBUDwKhUso'
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['blockschema'])
# def send_block_schema(message):
#     try:
#         with open("block-shema.jpeg", "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Блок-схема не найдена.")
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


# # Команда /calculate
# @bot.message_handler(commands=['calculate'])
# def ask_for_number(message):
#     bot.send_message(message.chat.id, "Введите число для перевода в двоичную систему:")
#     # Сохраняем состояние ожидания
#     bot.register_next_step_handler(message, convert_to_binary)

# def convert_to_binary(message):
#     try:
#         number = int(message.text)
#         binary_representation = bin(number)[2:]  # Преобразуем в двоичное
#         bot.send_message(message.chat.id, f"Двоичное представление: {binary_representation}")
#     except ValueError:
#         bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")
#         # Запрашиваем число снова
#         ask_for_number(message)

# # Команда /example
# @bot.message_handler(commands=['example'])
# def send_example(message):
#     bot.send_message(message.chat.id, "Пример: 42 в двоичной системе — это 101010.")

# # Запуск бота
# if __name__ == '__main__':
#     bot.polling()





# import telebot
# import os

# # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
# TOKEN = '7646993468:AAEJ4aRU8g21Ym9fEZ5v1rttGBBUDwKhUso'
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     welcome_text = (
#         "Привет! Я NumberVisualizerBot. Я могу помочь вам переводить числа между различными системами счисления.\n\n"
#         "Доступные команды:\n"
#         "/blockschema - Отправить блок-схему\n"
#         "/convert - Перевести число между системами счисления\n"
#         "/example - Привести пример\n"
#     )
#     bot.send_message(message.chat.id, welcome_text)


# @bot.message_handler(commands=['blockschema'])
# def send_block_schema(message):
#     try:
#         with open("block-shema.jpeg", "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Блок-схема не найдена.")
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# # Команда /convert
# @bot.message_handler(commands=['convert'])
# def ask_for_conversion(message):
#     bot.send_message(message.chat.id, "Введите число и укажите системы счисления в формате: число, от_системы, в_систему.\nПример: 1010, 2, 10")
#     bot.register_next_step_handler(message, convert_number)

# def convert_number(message):
#     try:
#         input_data = message.text.split(',')
#         number = input_data[0].strip()
#         from_base = int(input_data[1].strip())
#         to_base = int(input_data[2].strip())

#         # Преобразование числа в десятичную систему
#         decimal_number = int(number, from_base)
#         # Преобразование в нужную систему счисления
#         if to_base == 10:
#             result = str(decimal_number)
#         else:
#             result = ""
#             while decimal_number > 0:
#                 result = str(decimal_number % to_base) + result
#                 decimal_number //= to_base

#         bot.send_message(message.chat.id, f"{number} из системы {from_base} в систему {to_base} равно: {result or '0'}")
#     except (ValueError, IndexError):
#         bot.send_message(message.chat.id, "Ошибка ввода. Убедитесь, что вы вводите данные в правильном формате.")
#         ask_for_conversion(message)

# # Команда /example
# @bot.message_handler(commands=['example'])
# def send_example(message):
#     bot.send_message(message.chat.id, "Пример: 1010, 2, 10 (это 10 в десятичной системе)")

# # Запуск бота
# if __name__ == '__main__':
#     bot.polling()




# import telebot
# import math
# import os

# # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
# TOKEN = '7646993468:AAEJ4aRU8g21Ym9fEZ5v1rttGBBUDwKhUso'
# bot = telebot.TeleBot(TOKEN)

# # Приветствие и список команд
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     welcome_text = (
#         "Привет! Я NumberVisualizerBot. Я могу помочь вам переводить числа между различными системами счисления.\n\n"
#         "Доступные команды:\n"
#         "/blockschema - Отправить блок-схему\n"
#         "/convert - Перевести число между системами счисления\n"
#         "/example - Привести пример\n"
#         "/checksin - Проверить точность функции sin(x)\n"
#     )
#     bot.send_message(message.chat.id, welcome_text)

# @bot.message_handler(commands=['blockschema'])
# def send_block_schema(message):
#     try:
#         with open("block-shema.jpeg", "rb") as photo:
#             bot.send_photo(message.chat.id, photo)
#     except FileNotFoundError:
#         bot.send_message(message.chat.id, "Блок-схема не найдена.")
#     except Exception as e:
#         bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# # Команда /convert
# @bot.message_handler(commands=['convert'])
# def ask_for_conversion(message):
#     bot.send_message(message.chat.id, "Введите число и укажите системы счисления в формате: число, от_системы, в_систему.\nПример: 1010, 2, 10")
#     bot.register_next_step_handler(message, convert_number)

# def convert_number(message):
#     try:
#         input_data = message.text.split(',')
#         number = input_data[0].strip()
#         from_base = int(input_data[1].strip())
#         to_base = int(input_data[2].strip())

#         # Преобразование числа в десятичную систему
#         decimal_number = int(number, from_base)
#         # Преобразование в нужную систему счисления
#         if to_base == 10:
#             result = str(decimal_number)
#         else:
#             result = ""
#             while decimal_number > 0:
#                 result = str(decimal_number % to_base) + result
#                 decimal_number //= to_base

#         bot.send_message(message.chat.id, f"{number} из системы {from_base} в систему {to_base} равно: {result or '0'}")
#     except (ValueError, IndexError):
#         bot.send_message(message.chat.id, "Ошибка ввода. Убедитесь, что вы вводите данные в правильном формате.")
#         ask_for_conversion(message)

# # Команда /example
# @bot.message_handler(commands=['example'])
# def send_example(message):
#     bot.send_message(message.chat.id, "Пример: 1010, 2, 10 (это 10 в десятичной системе)")

# # Команда /checksin
# @bot.message_handler(commands=['checksin'])
# def check_sine_accuracy(message):
#     values = [1.0, 1.5, 2.0, 3.0, 3.14159, 6.28318]  # разные значения x
#     results = "Исследование точности функции sin(x):\n\n"
#     results += "{:<15} {:<30} {:<30}\n".format("x", "sin(x) (math)", "sin(x) (вывод с точностью)")

#     for x in values:
#         sin_math = math.sin(x)
#         results += "{:<15} {:<30} {:<30}\n".format(x, sin_math, f"{sin_math:.15f}")

#     bot.send_message(message.chat.id, results)

# # Запуск бота
# if __name__ == '__main__':
#     bot.polling()


import telebot
import math
import os

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен
TOKEN = '7646993468:AAEJ4aRU8g21Ym9fEZ5v1rttGBBUDwKhUso'
bot = telebot.TeleBot(TOKEN)

# Приветствие и список команд
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Привет! Я NumberVisualizerBot. Я могу помочь вам с изучением числовых методов.\n\n"
        "Доступные команды:\n"
        "/blockschema - Отправить блок-схему\n"
        "/convert - Перевести число между системами счисления\n"
        "/example - Привести пример\n"
        "/checksin - Проверить точность функции sin(x)\n"
        "/checkprecision - Проверить точность округления\n"
        "/checksubtraction - Проверить потерю точности при вычитании\n"
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['blockschema'])
def send_block_schema(message):
    try:
        with open("block.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Блок-схема не найдена.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

# Команда /convert
@bot.message_handler(commands=['convert'])
def ask_for_conversion(message):
    bot.send_message(message.chat.id, "Введите число и укажите системы счисления в формате: число, от_системы, в_систему.\nПример: 1010, 2, 10")
    bot.register_next_step_handler(message, convert_number)

def convert_number(message):
    try:
        input_data = message.text.split(',')
        number = input_data[0].strip()
        from_base = int(input_data[1].strip())
        to_base = int(input_data[2].strip())

        # Преобразование числа в десятичную систему
        decimal_number = int(number, from_base)
        # Преобразование в нужную систему счисления
        if to_base == 10:
            result = str(decimal_number)
        else:
            result = ""
            while decimal_number > 0:
                result = str(decimal_number % to_base) + result
                decimal_number //= to_base

        bot.send_message(message.chat.id, f"{number} из системы {from_base} в систему {to_base} равно: {result or '0'}")
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, "Ошибка ввода. Убедитесь, что вы вводите данные в правильном формате.")
        ask_for_conversion(message)

# Команда /example
@bot.message_handler(commands=['example'])
def send_example(message):
    bot.send_message(message.chat.id, "Пример: 1010, 2, 10 (это 10 в десятичной системе)")

# Команда /checksin
@bot.message_handler(commands=['checksin'])
def check_sine_accuracy(message):
    values = [1.0, 1.5, 2.0, 3.0, 3.14159, 6.28318]  # разные значения x
    results = "Исследование точности функции sin(x):\n\n"
    results += "{:<15} {:<30} {:<30}\n".format("x", "sin(x) (math)", "sin(x) (вывод с точностью)")

    for x in values:
        sin_math = math.sin(x)
        results += "{:<15} {:<30} {:<30}\n".format(x, sin_math, f"{sin_math:.15f}")

    bot.send_message(message.chat.id, results)

# Команда /checkprecision
@bot.message_handler(commands=['checkprecision'])
def ask_for_precision(message):
    bot.send_message(message.chat.id, "Введите дробное число (например, 1/3):")
    bot.register_next_step_handler(message, check_precision)

def check_precision(message):
    try:
        # Получаем дробное значение от пользователя
        input_value = eval(message.text)  # Используем eval для вычисления выражения
        float_sum = float(input_value) + float(input_value) + float(input_value)
        double_sum = (input_value) + (input_value) + (input_value)  # В Python float и double имеют одинаковую точность
        
        result = (
            "Проверка точности округления:\n"
            f"Float sum: {float_sum}\n"
            f"Double sum: {double_sum}\n"
        )
        bot.send_message(message.chat.id, result)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}. Пожалуйста, попробуйте еще раз.")

# Команда /checksubtraction
@bot.message_handler(commands=['checksubtraction'])
def ask_for_subtraction(message):
    bot.send_message(message.chat.id, "Введите первое число (например, 1.000001):")
    bot.register_next_step_handler(message, get_second_number)

def get_second_number(message):
    try:
        x1 = float(message.text)
        bot.send_message(message.chat.id, "Введите второе число (например, 1.000000):")
        bot.register_next_step_handler(message, lambda msg: check_subtraction(x1, msg))
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите корректное число.")

def check_subtraction(x1, message):
    try:
        x2 = float(message.text)
        result = x1 - x2
        bot.send_message(message.chat.id, f"Результат вычитания {x1} - {x2} = {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите корректное число.")



# Запуск бота
if __name__ == '__main__':
    bot.polling()

