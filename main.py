import requests
from datetime import datetime
import json
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6479298908:AAFIv2dXPGzulLBI1NXAWZuplISuEM2VpFA'
BOT_USERNAME = '@Fireflymemesbot'



# Create commands
async def command_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print(update.message)
    await update.message.reply_text("Vamos")

async def command_get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fetching the best video")


# A function to generate responses depending on the text that the user sends.
def message_responses(text):
    if True in [True if word in text.lower() else False for word in ['hello', 'hi', 'hey', 'good morning', "Good evening"]]:
        return 'Hello. How are you'

    elif True in [True if word in text.lower() else False for word in ['wozza', 'niaje', 'rada', 'alo', "semaje"]]:
        return 'Wozza wozza. Nichapie'

    elif True in [True if word in text.lower() else False for word in ['time is it', 'current time', 'time now', 'time']]:
        return f'It is currently {datetime.now().time()} in Nairobi, Kenya'

    elif True in [True if word in text.lower() else False for word in ['sai ni saa', 'time sai']]:
        return f'Sai ni {datetime.now().time()} huku Kanairo.'
    else:
        return f'I cannot understand you'


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # message_type: either group or direct chat
    message_type = update.message.chat.type
    print(update)

    # the text itself
    text = update.message.text

    print(f'User: {update.message.chat.id} in {message_type}: {text}')

    sent_video_id = update.message.video.file_id

    response = f'Thanks for the vid {update.message.chat.first_name}'

    print(f'Bot: {response}')

    await update.message.reply_video(sent_video_id, reply_to_message_id=update.message.id, caption='Chasing da bag yorona')



# A function to handle incoming text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # message_type: either group or direct chat
    message_type = update.message.chat.type
    print(update)

    # the text itself
    text = update.message.text

    print(f'User: {update.message.chat.id} in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = message_responses(new_text)
        else:
            return

    else:
        response = message_responses(text)

    print(f'Bot: {response}')

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Create the bot app and run it
if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()

    # add command handlers for bot commands
    app.add_handler(CommandHandler('start', command_start))
    app.add_handler(CommandHandler('get', command_get))

    # add message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))

    # Add error handler
    app.add_error_handler(error)
    print('Polling...')
    app.run_polling()




# Notes:
# Set Commands on botfather

# Give the bot admin previledges for it to respond to messages




            











