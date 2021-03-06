from django.conf import settings
from django.core.mail import send_mail # EmailMessage
from django.db import models
from django.urls import reverse
from django.template.loader import render_to_string


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=150)

    def __str__(self):
        return str(self.stripe_id)


class EmailConfirmed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def activate_user_email(self):
        # activation_usrl = "http://localhost:8000/accounts/accounts/activate/%s" %(self.activation_key)
        activation_usrl = "%s/%s/" %(settings.DEFAULT_SITE_URL, reverse("accounts:activation_view", args=[self.activation_key]))
        context = {
            "activation_key": self.activation_key,
            "activation_usrl": activation_usrl,
            "user": self.user.username
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your email"
        #print(message)
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], kwargs)
        # email = EmailMessage(subject, message, from_email, [self.user.email], **kwargs)
        # email.send()