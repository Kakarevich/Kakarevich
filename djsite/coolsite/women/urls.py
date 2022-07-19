from django.urls import path, re_path # Импортируем path для формирования маршрутов

from .views import * # Импортируем из пакета women views все функции представления

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/ т.к. в coolsite/urls.py мы указали path('women/', include('women.urls'))
    path('cats/<slug:catid>/', categories), # http://127.0.0.1:8000/cats/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]