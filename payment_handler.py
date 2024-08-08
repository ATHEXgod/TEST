import razorpay
from config.settings import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET, PAYMENT_FEATURE_ENABLED

if PAYMENT_FEATURE_ENABLED:
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

    def create_payment_order(amount, user_id):
        order = client.order.create({
            "amount": amount * 100,  # Amount in paise
            "currency": "INR",
            "payment_capture": '1'
        })
        return order

    def verify_payment(payment_id, order_id, signature):
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            return True
        except:
            return False
else:
    def create_payment_order(amount, user_id):
        raise NotImplementedError("Payment feature is disabled")

    def verify_payment(payment_id, order_id, signature):
        raise NotImplementedError("Payment feature is disabled")
