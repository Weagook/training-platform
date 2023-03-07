from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexMain(request):
    return HttpResponse('Главная страница сайта')