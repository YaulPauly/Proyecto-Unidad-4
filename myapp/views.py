from django.shortcuts import render, redirect #La funcion render nos ayudara a utilizar los templates
from django.views.generic import View, TemplateView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Portafolio 
from .forms import PortafolioForm

class Index(TemplateView):
    template_name = "index.html"
    extra_context = {"portafolios": Portafolio.objects.all()}

class Home(LoginRequiredMixin,TemplateView):
    template_name = "home.html"
    extra_context = {
        "portafolios": Portafolio.objects.all(),
        "users": User.objects.all()
    }

class CreatePortafolio(LoginRequiredMixin, FormView):
    template_name = "portafolio/create.html"
    model = Portafolio
    form_class = PortafolioForm

    def form_valid(self, form):
        Portafolio.objects.create(**form.cleaned_data)
        return redirect('../home/')

class VistaPortafolio(LoginRequiredMixin,TemplateView):
    template_name = "portafolio/details.html"
    extra_context = {"portafolios": Portafolio.objects.all()}

    

