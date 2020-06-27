from django.contrib import admin
from .models import MarketingMessage

class MarketingMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)