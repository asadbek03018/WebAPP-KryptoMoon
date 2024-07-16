from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import KryptoExchanges

# Create your views here.
@require_http_methods(["GET", "POST"])
def exchanger(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        telegram_username = request.POST.get('username')
        credit_card = request.POST.get('credit_card')
        credit_card_holder = request.POST.get('credit_card_placeholder')
        from_currency = request.POST.get('valyuta')
        to_currency = request.POST.get('uzs')

        if all([amount,telegram_username, credit_card, credit_card_holder, from_currency, to_currency]):
            # Bu yerda siz ma'lumotlarni saqlash, valyuta ayirboshlash operatsiyasini
            # bajarish yoki boshqa kerakli amallarni bajarishingiz mumkin
            exchange = KryptoExchanges(
                amount=amount,
                telegram_username=telegram_username,
                credit_card=credit_card,
                credit_card_placeholder=credit_card_holder,
                valyuta=from_currency,
                uzs=to_currency
            )
            exchange.save()
            # Misol uchun, foydalanuvchiga xabar yuborish
            data = {'xabar': "Sizning so'rovingiz bazaga qo'shildi! Admin javobini kuting"}
        else:
            data = {'xabar': "Iltimos barcha maydonlarni to'ldiring!"}

        return render(request, 'exchanger.html', data)
    return render(request, 'exchanger.html')