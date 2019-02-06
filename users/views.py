# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy,reverse

from forms import RegistroForm





# Create your views here.
def index(request):
    #Se renderiza un html harcode
    #return HttpResponse("Index")
    return render(request,'users/index.html')



class UserRegistration(CreateView):
    model= User
    template_name="users/registry.html"
    #form_class= UserCreationForm  # se realiza el siguientre cambio para mejorar el formulario
    form_class= RegistroForm
    success_url = reverse_lazy("custommer:custommer_list")
