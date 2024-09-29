package main

import (
	"fmt"
	"log"
	"os"
	"strconv"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

func main() {
	bot, err := tgbotapi.NewBotAPI("7646993468:AAEJ4aRU8g21Ym9fEZ5v1rttGBBUDwKhUso")
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("Authorized on account %s", bot.Self.UserName)

	updates, err := bot.GetUpdatesChan(tgbotapi.UpdateConfig{Offset: 0, Limit: 100, Timeout: 60})

	for update := range updates {
		if update.Message == nil { // ignore non-message updates
			continue
		}

		command := update.Message.Text

		switch command {
		case "/blockschema":
			sendBlockSchema(bot, update.Message.Chat.ID)
		case "/calculate":
			askForNumber(bot, update.Message.Chat.ID)
		case "/example":
			sendExample(bot, update.Message.Chat.ID)
		default:
			sendHelp(bot, update.Message.Chat.ID)
		}
	}
}

func sendBlockSchema(bot *tgbotapi.BotAPI, chatID int64) {
	photoPath := "block_schema.png" // Замените на свой путь

	// Проверка существования файла
	if _, err := os.Stat(photoPath); os.IsNotExist(err) {
		log.Printf("Файл не найден: %s", err)
		return
	}

	// Используем NewPhotoShare для отправки фото
	photo := tgbotapi.NewPhotoShare(chatID, photoPath)

	if _, err := bot.Send(photo); err != nil {
		log.Printf("Ошибка при отправке блок-схемы: %s", err)
	}
}

func askForNumber(bot *tgbotapi.BotAPI, chatID int64) {
	msg := tgbotapi.NewMessage(chatID, "Введите число для перевода в двоичную систему:")
	bot.Send(msg)

	updates, _ := bot.GetUpdatesChan(tgbotapi.UpdateConfig{Offset: 0, Limit: 100, Timeout: 60})
	for update := range updates {
		if update.Message == nil || update.Message.Chat.ID != chatID {
			continue
		}

		number, err := strconv.Atoi(update.Message.Text)
		if err != nil {
			msg := tgbotapi.NewMessage(chatID, "Пожалуйста, введите корректное число.")
			bot.Send(msg)
			return
		}

		binaryRepresentation := strconv.FormatInt(int64(number), 2)
		msg := tgbotapi.NewMessage(chatID, fmt.Sprintf("Двоичное представление: %s", binaryRepresentation))
		bot.Send(msg)
		break
	}
}

func sendExample(bot *tgbotapi.BotAPI, chatID int64) {
	msg := tgbotapi.NewMessage(chatID, "Пример: 42 в двоичной системе — это 101010.")
	bot.Send(msg)
}

func sendHelp(bot *tgbotapi.BotAPI, chatID int64) {
	msg := tgbotapi.NewMessage(chatID, "Доступные команды:\n/blockschema - Вывести блок-схему\n/calculate - Выполнить расчет\n/example - Вывести пример")
	bot.Send(msg)
}
