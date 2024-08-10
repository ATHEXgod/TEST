import os

API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN', '7242067053:AAHLoLKbLZhAcPzmmEIPcDQCxmVtk1iKsKU')  # Set your Telegram Bot API token
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID', 'your_default_key_id')  # Set your Razorpay Key ID
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET', 'your_default_key_secret')  # Set your Razorpay Key Secret
MONGO_DB_URI = os.getenv('MONGO_DB_URI', 'mongodb+srv://moditrathor:4BG38960UgCWZXbS@cluster0.sdkc4bt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Set your MongoDB URI
PAYMENT_FEATURE_ENABLED = os.getenv('PAYMENT_FEATURE_ENABLED', 'False').lower() == 'true'  # Set to True or False
# config/settings.py

OWNER_ID = 20478027  # Replace with the actual Telegram user ID
