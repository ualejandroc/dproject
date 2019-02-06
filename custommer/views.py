# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers

######
from django.http import HttpResponse, HttpResponseRedirect
from custommer.forms import CustommerForms,ApplicationForms
from models import Custommer, Application


def listado(request):
    lista=serializers.serialize('json',Custommer.objects.all())
    return HttpResponse(lista,content_type='application/json')



# Create your views here.
def index(request):
    #Se renderiza un html harcode
    #return HttpResponse("Index")
    return render(request,'custommer/index.html')



def custommer_View(request):
    if request=="POST":
        form=CustommerForms(request.POST)
        if form.is_valid():
            form.save()
        return reverse_lazy('custommer/custommer_list.html')

    else :
        form=CustommerForms()
        return render(request,'custommer/custommer_form.html', {'form':form})


def lista(request):
    #Se renderiza un html harcode
    #return HttpResponse("Index")
    custommers=None
    contexto=None

    custommers=Custommer.objects.all() 
    contexto= {'custommers':custommers}

    return render(request,'custommer/custommer_list.html', contexto)


def custommer_edit(request, id_custommer):
    custommer=None
    custommer= Custommer.objects.get(id=id_custommer)
    if request.method=='GET':
        form= CustommerForms(instance=custommer )
    else:
        form=CustommerForms(request.POST, instance=custommer)
        if form.is_valid():
            form.save()
        return redirect('/custommer/lista')
    return render(request,'custommer/custommer_form.html', {'form':form} )


def custommer_delete(request, id_custommer):
    custommer=None
    custommer= Custommer.objects.get(id=id_custommer)
    if request.method=='POST':
        custommer.delete()
        return reverse_lazy('custommer/custommer_list.html')
    return   render(request, 'custommer/custommer_delete.html', {'custommer':custommer})




class CustommerView(ListView):
    model= Custommer
    template_name='custommer/custommer_list.html'
    paginate_by=2



class CustommerCreate(CreateView):
    model=Custommer
    form_class=CustommerForms
    template_name='custommer/custommer_form.html'
    success_url=reverse_lazy('custommer:custommer_list')


class CustommerUpdate(UpdateView):
    model=Custommer
    form_class=CustommerForms
    template_name='custommer/custommer_form.html'
    success_url=reverse_lazy('custommer:custommer_list')


class CustommerDelete(DeleteView):
    model=Custommer
    template_name='custommer/custommer_delete_class.html'
    success_url=reverse_lazy('custommer:custommer_list')





class ApplicationList(ListView):
    model= Application
    template_name='application/application_list.html'

class ApplicationCreate(CreateView):
    model=Application
    form_class=ApplicationForms
    second_form_class=CustommerForms
    template_name='application/application_form.html'
    success_url=reverse_lazy('application:application_list')



    def get_context_data(self,**kwargs):
        context=super(ApplicationCreate,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)

        return context


    def post(self,request,*args,**kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            application =form.save(commit=False)
            application.custommer=form2.save()
            application.save()
            return HttpResponseRedirect(self.get_succes_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))



class ApplicationUpdate(UpdateView):
    model=Application
    second_model=Custommer
    form_class=ApplicationForms
    second_form_class=CustommerForms
    template_name='custommer/custommer_form.html'
    success_url=reverse_lazy('application:application_list')

    def get_context_data(self,**kwargs):
        context=super(ApplicationCreate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        application = self.objects.get(id=pk)
        cuatommer= self.second_model.objects.get(id=application.custommer_id)

        if 'form' not in context:
            context['form']=self.form_class()
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=custommer)
        context['id']=pk
        return context

    def post(self,request,*args,**kwargs):
        self.object=self.get_object
        id_application=kwargs['pk']
        application= self.model.objects.get(id=id_application)
        application= self.second_model.objects.get(id=application.custommer_id)
        form=self.form_class(request.POST, instance=application)
        form2=self.second_form_class(request.POST, instance=custommer)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_succes_url())
        else:
            return HttpResponseRedirect(self.get_succes_url())





class ApplicationDelete(DeleteView):
    model=Application
    template_name='application/applicartion_delete.html'
    success_url=reverse_lazy('application:application_list')