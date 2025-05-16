from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Today", callback_data='today'),
            InlineKeyboardButton("Yesterday", callback_data='yesterday'),
            InlineKeyboardButton("Tomorrow", callback_data='tomorrow')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Which day menu do you want?", 
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  

    day_choice = query.data
    if day_choice == 'today':
        response = "You chose *Today*'s menu!"
    elif day_choice == 'yesterday':
        response = "You chose *Yesterday*'s menu!"
    elif day_choice == 'tomorrow':
        response = "You chose *Tomorrow*'s menu!"
    else:
        response = "Unknown option!"

    await query.edit_message_text(text=response)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

