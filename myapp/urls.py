from django.urls import path
from . import views #Importo las funciones del archivo views.py


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home/', views.Home.as_view(), name='home'),
    path('home/portafolio-details/<title_proyecto>', views.VistaPortafolio.as_view(), name='portafolio' ),
    path('crear-portafolio/', views.CreatePortafolio.as_view(), name='crear' ),
         

]