import datetime
from data.database import db

subscriptions = db['subscriptions']

def is_subscribed(user_id):
    user = subscriptions.find_one({"user_id": user_id})
    if user and user['expiry_date'] > datetime.datetime.now():
        return True
    return False

def add_subscription(user_id, days):
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=days)
    subscriptions.update_one(
        {"user_id": user_id},
        {"$set": {"expiry_date": expiry_date}},
        upsert=True
    )
# bot/subscription_manager.py

def set_role(user_id, role):
    roles.update_one(
        {"user_id": user_id},
        {"$set": {"role": role}},
        upsert=True
    )

def get_role(user_id):
    user = roles.find_one({"user_id": user_id})
    return user['role'] if user else None
