from django.shortcuts import render
from .models import Humans

def index(request):
    humans = Humans.objects.all()
    cont={'humans': humans,'title': 'Список людей'}
    return render(request, 'humans_index.html', context=cont)
