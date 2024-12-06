import stripe

stripe.api_key = "your_secret_key"


def process_payment(amount, currency="usd"):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount * 100,  # Amount in cents
            currency=currency,
        )
        return payment_intent
    except stripe.error.StripeError as e:
        return {"error": str(e)}
