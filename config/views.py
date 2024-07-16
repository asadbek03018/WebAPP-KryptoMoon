from django.shortcuts import render
from home.models import SliderServices, OurServices, CustomersSays

def home(request):
    data = {
        'sliders': SliderServices.objects.all(),
        'services': OurServices.objects.all(),
        'customers': CustomersSays.objects.all()
    }
    return render(request, 'index.html', data)