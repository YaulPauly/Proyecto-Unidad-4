from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login #Nos provee de la clase LoginView que esta predefinida para el login
from .views import RegisterView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout', logout_then_login, name='logout')
]

#LoginView
#recibe 2 parametros, username y password
#va a buscar el archivo registration/login 
#template_name = "registration/login"
# la url se debe llamar accounts/login/

