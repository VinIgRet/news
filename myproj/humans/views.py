from django.shortcuts import render
from .models import Humans,Professions
from .forms import PersonForm
from django.shortcuts import redirect

def index(request):
    humans = Humans.objects.all()
    cont={'humans': humans,'title': 'Список людей'}
    return render(request, 'humans/index.html', context=cont)

def getprof(request, profid):
    humans = Humans.objects.filter(profession_id=profid)
    prof=Professions.objects.get(pk=profid)
    cont={'humans': humans,'title': f'Персоны с профессией: \"{prof.title}\"'}
    return render(request, 'humans/index.html', context=cont)

def gethumans(request, humansid):
    item = Humans.objects.get(pk=humansid)
    return render(request, 'humans/person.html', {'item': item,'title': item.famil+' '+item.name+' '+item.otches})

def addperson(request):
    if request.method == 'POST':
        form=PersonForm(request.POST, request.FILES)
        if form.is_valid():
            human=form.save()
            return redirect('allhumans')
    else:
        form = PersonForm()
        return render(request, 'humans/addperson.html', {'form': form,'title': 'Добавление персоны'}) 