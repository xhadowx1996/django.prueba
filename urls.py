from .views import RegisterAPI ,LoginAPI,postCreateClientes,excels,produtos
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('api/Registro/', RegisterAPI.as_view(), name='Registro'),
    path('api/Acceso/', LoginAPI.as_view(), name='Acceso'),
    path('api/Salir/', knox_views.LogoutView.as_view(), name='Salir'),
    path('api/Evacuar/', knox_views.LogoutAllView.as_view(), name='Evacuar'),
    path('api/CrearClientes',postCreateClientes, name='CrearClientes'),
    path('api/Descarge',excels,name='Descarge'),
    path('api/Productos',produtos,name='Productos')
]
