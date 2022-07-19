from django.urls import path # Импортируем path для формирования маршрутов

from .views import * # Импортируем из пакета women views все функции представления

urlpatterns = [
    path('', index)  # http://127.0.0.1:8000/women/ т.к. в coolsite/urls.py мы указали path('women/', include('women.urls'))
    path('cats/', categories) # http://127.0.0.1:8000/women/cats/
]