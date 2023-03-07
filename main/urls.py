from django.urls import path

from .views import *

urlpatterns = [
    path('', indexMain),
    path('level/<int:lvlid>/', indexLevel)
]