from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def indexMain(request):
    print(request.GET)
    return HttpResponse('Главная страница сайта')


def indexLevel(request, lvlid):
    return HttpResponse(f'<h1>Уровень номер {lvlid}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена. Ошибка 404.</h1>')
