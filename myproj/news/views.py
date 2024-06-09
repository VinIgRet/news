from django.shortcuts import render
from django.http import HttpResponse
from .models import News, NewsCategory
from .forms import NewsForm
from django.shortcuts import redirect

def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список главных новостей'})

def getcat(request, catid):
    news = News.objects.filter(category_id=catid)
    cat = NewsCategory.objects.get(pk=catid)
    return render(request, 'news/index.html', {'news': news, 'title': f'Список новостей категории {cat.title}'})

def getnews(request, newsid):
    item = News.objects.get(pk=newsid)
    return render(request, 'news/detail.html', {'item': item,"title": item.title})

def addnews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect('allnews')
    else:
        form = NewsForm()
        return render(request, 'news/addnews.html', {'form': form, 'title': 'Добавление новости'})