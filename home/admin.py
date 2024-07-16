from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import SliderServices, OurServices, CustomersSays, KryptoExchanges
# Register your models here.
admin.site.register(SliderServices)
admin.site.register(OurServices)
admin.site.register(CustomersSays)

@admin.register(KryptoExchanges)
class KryptoExchangesAdmin(ModelAdmin):
    list_display = ('id', 'valyuta', 'uzs', 'amount', 'telegram_username', 'credit_card', 'credit_card_placeholder')
    list_filter = ('valyuta', )
    list_display_links = ('id', 'valyuta', 'uzs')