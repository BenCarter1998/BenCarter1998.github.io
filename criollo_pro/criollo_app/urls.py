from django.urls import path
from . import views

urlpatterns = [
    path('', views.criollo, name='criollo'),
    # Puedes agregar más rutas según sea necesario
]
