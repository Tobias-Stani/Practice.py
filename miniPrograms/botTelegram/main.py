from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Inserta tu token aquí
TOKEN = '7791648800:AAEswTQNdBBsTyuIwgkDf1841Xm76ML3jAU'


# Función para iniciar el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu nuevo bot. ¿En qué puedo ayudarte?')

# Función para responder a mensajes de texto
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    await update.message.reply_text(f"Recibí tu mensaje: {user_message}")

# Configuración principal del bot
def main():
    application = Application.builder().token(TOKEN).build()
    
    # Registrar el comando /start
    application.add_handler(CommandHandler("start", start))
    
    # Registrar el manejador de mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
