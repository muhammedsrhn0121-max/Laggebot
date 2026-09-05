import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Loglama ayarları
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Premium kullanıcıların Telegram ID'lerini buraya ekleyebilirsin
PREMIUM_USERS = [123456789]  # Kendi Telegram ID'ni buraya yazabilirsin

# /laggev1 komutu (Sadece Premium - Phishing framework simülasyonu)
async def laggev1_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in PREMIUM_USERS:
        await update.message.reply_text("Bu komut yalnızca **Premium** kullanıcılara özeldir! 🔒")
        return
    
    menu_text = (
        "=== Lagge v1.0 Custom Phishing Framework ===\n\n"
        "[::] Hedef Şablonu Seçin [::]\n"
        "[01] Instagram\n"
        "[02] Netflix\n"
        "[03] TikTok\n"
        "[04] Xbox\n"
        "[05] Facebook\n"
        "[00] Çıkış"
    )
    await update.message.reply_text(menu_text)

# /laggenick komutu (Ücretsiz)
async def laggenick_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Mevcut kullanıcı adınız: {user_name} (LaggeNick aktif)")

# /laggeipcall komutu (Ücretsiz - Ağ ve konum bilgi sorgulama simülasyonu)
async def laggeipcall_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        target_ip = context.args[0]
        result = (
            f"--- LaggeIPCall Ağ ve Konum Bilgi Sorgulama ---\n"
            f"[+] '{target_ip}' için IP sorgulaması başlatılıyor...\n\n"
            f"[*] IP Adresi : {target_ip}\n"
            f"[*] Ülke : Turkey (TR)\n"
            f"[*] Şehir : İstanbul\n"
            f"[*] Servis Sağl. : Vodafone / Telekom"
        )
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Lütfen bir IP adresi girin. Örnek: /laggeipcall 212.115.7.108")

def main():
    TOKEN = "8927427712:AAEFaIt5V_nXyFe_S"
    
    app = ApplicationBuilder().token(TOKEN).build()

    # Komut yönlendiricileri
    app.add_handler(CommandHandler("laggev1", laggev1_command))
    app.add_handler(CommandHandler("laggenick", laggenick_command))
    app.add_handler(CommandHandler("laggeipcall", laggeipcall_command))

    print("Bot başlatılıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
