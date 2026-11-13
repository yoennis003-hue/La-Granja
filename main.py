
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Bienvenido a mi juego de granja.")
if name == 'main':
application = ApplicationBuilder().token('9151634765:AAGvj2NtjKgu6dFVBgk6fB_7xS-zq_9uozQ').build()
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
application.run_polling()

