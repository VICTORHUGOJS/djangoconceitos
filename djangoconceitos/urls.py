from django.contrib import admin
from django.urls import path, include
from clientes import urls as clients_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', include(clients_urls)), #chamar a urls do app
]
