import stripe
from config import settings

stripe.api_key = settings.stripe_secret_key


def main():
    checkout_session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_email="edward.elric@exaple.com",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": "10000",
                    "product_data": {
                        "name": "Philosopher's Stone",
                    },
                },
                "quantity": 1,
            }
        ],
        success_url=settings.payment_success_url,
        cancel_url=settings.payment_cancel_url,
        metadata={
            "session_id": "13435",
        },
    )

    print(checkout_session)



if __name__ == '__main__':
    main()
