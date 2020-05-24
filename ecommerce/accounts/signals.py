import stripe
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# customer id stripe
# cus_HL0rkyglKZyDS0
# cus_HL18MPqy80MqZe
def get_or_create_stripe(sender, user, *args, **kwargs):
    print("sender")
    # print(user.email) # user
    try:
        user.userstripe.stripe_id
        # print("\n", "TRY", "\n")
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email=str(user.email)
        )
        new_user_stripe = UserStripe.objects.create(
            user=user, stripe_id=customer.id)
        # print("\n", "NOT EXIST", "\n")
    except:
        # print("\n", "PASS", "\n")
        pass


user_logged_in.connect(get_or_create_stripe)
