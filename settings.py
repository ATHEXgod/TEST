import os

API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN', 'your_default_bot_token')  # Set your Telegram Bot API token
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID', 'your_default_key_id')  # Set your Razorpay Key ID
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET', 'your_default_key_secret')  # Set your Razorpay Key Secret
MONGO_DB_URI = os.getenv('MONGO_DB_URI', 'your_default_mongo_uri')  # Set your MongoDB URI
PAYMENT_FEATURE_ENABLED = os.getenv('PAYMENT_FEATURE_ENABLED', 'False').lower() == 'true'  # Set to True or False
# config/settings.py

OWNER_ID = 123456789  # Replace with the actual Telegram user ID
