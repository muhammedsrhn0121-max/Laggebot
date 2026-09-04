import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8927427721:AAEFaIt5V_nXyFe_Seobqpt42GrxYQQs_iY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selam! Lagge Suite botu aktif ve çalışıyor.")

def main():
    app = ApplicationBuilder().token(TOKEN).connect_timeout(60).read_timeout(60).write_timeout(60).build()
    app.add_handler(CommandHandler("start", start))
    
    print("[*] Bot baslatiliyor, Telegram ile baglanti kuruluyor...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
