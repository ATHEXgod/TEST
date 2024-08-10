import telebot
from config.settings import API_TOKEN, PAYMENT_FEATURE_ENABLED
from bot.payment_handler import create_payment_order, verify_payment
from bot.subscription_manager import is_subscribed, add_subscription

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /subscribe to get a premium subscription.")

@bot.message_handler(commands=['subscribe'])
def handle_subscribe(message):
    if PAYMENT_FEATURE_ENABLED:
        user_id = message.from_user.id
        order = create_payment_order(100, user_id)  # Example: 100 INR for a subscription
        bot.send_message(user_id, f"Please complete the payment using this link: {order['short_url']}")
    else:
        bot.reply_to(message, "Payment feature is currently disabled.")

@bot.message_handler(commands=['verify_payment'])
def handle_payment_verification(message):
    if PAYMENT_FEATURE_ENABLED:
        user_id = message.from_user.id
        payment_id = message.text.split()[1]
        order_id = message.text.split()[2]
        signature = message.text.split()[3]
        
        if verify_payment(payment_id, order_id, signature):
            add_subscription(user_id, 30)  # Add 30 days subscription
            bot.send_message(user_id, "Subscription successful! Enjoy ad-free access.")
        else:
            bot.send_message(user_id, "Payment verification failed. Please try again.")
    else:
        bot.reply_to(message, "Payment feature is currently disabled.")

@bot.message_handler(commands=['access_content'])
def handle_access_content(message):
    user_id = message.from_user.id
    if is_subscribed(user_id):
        bot.send_message(user_id, "Here is your content: [Link]")
    else:
        bot.send_message(user_id, "Please complete this ad task to access the content: [Ad Link]")
# bot/main.py

from bot.subscription_manager import set_role, get_role

@bot.message_handler(commands=['set_admin'])
def set_admin(message):
    owner_id = message.from_user.id
    if get_role(owner_id) == "Owner":
        admin_id = message.text.split()[1]
        set_role(admin_id, "Admin")
        bot.reply_to(message, f"User {admin_id} is now an Admin.")
    else:
        bot.reply_to(message, "Only the Owner can assign Admin roles.")

@bot.message_handler(commands=['admin_action'])
def admin_action(message):
    if get_role(message.from_user.id) in ["Admin", "Owner"]:
        # Perform admin action
        bot.reply_to(message, "Admin action performed.")
    else:
        bot.reply_to(message, "You don't have permission to perform this action.")


bot.polling()
