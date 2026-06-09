import os
from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.getenv("")

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    try:
        await update.chat_join_request.approve()

        await context.bot.send_message(
            chat_id=user.id,
            text="✅ Your VIP join request approved.\n\nWelcome to FFM VIP 💎"
        )

        print(f"Approved and messaged: {user.id} - {user.first_name}")

    except Exception as e:
        print("Error:", e)

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN missing in Railway Variables")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request))

    print("Bot started on Railway...")
    app.run_polling()

if __name__ == "__main__":
    main()
