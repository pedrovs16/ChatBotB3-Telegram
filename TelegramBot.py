# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler
import yfinance as yf


def main():
    # Start bot

    print('Start bot')
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('papel', start))
    # Start bot
    updater.start_polling()
    updater.idle()


def start(update, context):
    try:
        # Search information

        text = context.args[0]
        company = text.upper()
        if company == '^BVSP':
            stock = yf.Ticker(company)
        else:
            stock = yf.Ticker(f"{company}.SA")
        wallet = stock.info
        try:
            dividend = float(wallet["dividendYield"]) * 100
            porcent = ((float(wallet["ask"])) / (float(wallet["previousClose"])) - 1) * 100

            # Sending message

            message = f'Nome da empresa: {wallet["shortName"]} \n' \
                      f'Cotação de ontem: {wallet["previousClose"]} \n' \
                      f' Cotação atual: {wallet["ask"]} \n' \
                      f'Variação: {round(porcent, 2)}%  \n' \
                      f' Dividend Yield: {round(dividend, 2)}%'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        except:
            porcent = ((float(wallet["ask"])) / (float(wallet["previousClose"])) - 1) * 100

            # Sending message

            message = f'Nome da empresa: {wallet["shortName"]} \n' \
                      f'Cotação de ontem: {wallet["previousClose"]} \n' \
                      f' Cotação atual: {wallet["ask"]} \n' \
                      f'Variação: {round(porcent, 2)}%  \n'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except:
        message = 'Papel inválido'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# Token that you can get talking with BotFather on Telegram
token = 'token'

main()