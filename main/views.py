from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


def indexMain(request):
    cards = Lesson.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'card': cards})


def indexLevel(request, lvlid):
    return HttpResponse(f'<h1>Уровень номер {lvlid}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
