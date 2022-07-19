from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:      # Добавили проверку
        #raise Http404()      # Генерируем ошибку 404
        return redirect('home', permament=True)  # Перешли на главную страницу, если условие выполнено. permament=True говорит, что 302 ошибка
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Бро, страница не найдена, а в правительстве сидят рептилоиды</h1>")