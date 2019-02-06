# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers

######
from django.http import HttpResponse, HttpResponseRedirect

from ai.matplot import make_fig

from ai.aitest import learnTest, aiTest1, aiTest2, aiTest3



# Create your views here.
def index(request):
    #Se renderiza un html harcode
    #return HttpResponse("Index") 
    #make_fig()

    #learnTest()

    # aiTest1()

    # aiTest2()

    aiTest3()

    return render(request,'arti/index.html')

