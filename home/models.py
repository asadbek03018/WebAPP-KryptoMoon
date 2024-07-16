from django.db import models

# Create your models here.
class SliderServices(models.Model):
    slider_title = models.CharField(max_length=200)
    slider_description = models.TextField()
    slider_image = models.ImageField(upload_to='slider/images/')
    slider_button = models.CharField(max_length=45)
    slider_button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.slider_title



class OurServices(models.Model):
    service_icon = models.ImageField(upload_to='service/images/')
    service_title = models.CharField(max_length=75)
    service_description = models.TextField()

    def __str__(self):
        return self.service_title


class CustomersSays(models.Model):
    customer_name = models.CharField(max_length=110)
    customer_location = models.CharField(max_length=100)
    customer_image = models.ImageField(upload_to='customers/images/')
    customer_message = models.TextField()

    def __str__(self):
        return self.customer_name

class KryptoExchanges(models.Model):
    amount = models.CharField(max_length=10000)
    telegram_username = models.CharField(max_length=95, blank=True, null=True)
    credit_card = models.CharField(max_length=80)
    credit_card_placeholder = models.CharField(max_length=80)
    valyuta = models.CharField(max_length=40)
    uzs = models.CharField(max_length=50)
