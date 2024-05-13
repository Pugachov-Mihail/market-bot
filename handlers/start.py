import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from service import report


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def but(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Отчет о продажах", callback_data="1"),
            InlineKeyboardButton("Остатки товара", callback_data="2"),
        ],
        [
            InlineKeyboardButton("Админка", callback_data="3")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Меню:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    if query.data == "1":
        result = report.report_sales()
        await query.edit_message_text(text=f"<b>Отчет по товарам:</b>\n {' '.join(result)} \n", parse_mode="HTML")
    if query.data == "2":
        await query.edit_message_text(text=f"Даблл пидор!!!")
    if query.data == "3":
        await query.edit_message_text(text="Долбаеб? Э")
