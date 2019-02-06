from django.conf.urls import url, include
from django.contrib import admin
from views import index, custommer_View, lista, custommer_edit, custommer_delete, \
    CustommerView,CustommerCreate, CustommerUpdate, CustommerDelete,ApplicationList,\
    ApplicationCreate, ApplicationUpdate, ApplicationDelete, listado


from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^index$', index),
    #url(r'^nuevo$', login_required( custommer_View ),name="custommer_create"),
    url(r'^nuevo$', CustommerCreate.as_view(),name="custommer_create"),
    url(r'^lista$', lista,name="custommer_list"),
    url(r'^lista_clase', CustommerView.as_view() ,name="custommer_list_class"),
    url(r'^editar/(?P<id_custommer>\d+)/$', custommer_edit,name="custommer_edit"),  
    url(r'^editar/(?P<pk>\d+)/$', CustommerUpdate.as_view(),name="custommer_edit_class"),  
    url(r'^eliminar/(?P<id_custommer>\d+)/$', custommer_delete,name="custommer_delete"),    
    url(r'^eliminar/(?P<pk>\d+)/$', CustommerDelete.as_view(),name="custommer_delete_class"), 

    url(r'^lista_solicitud$', ApplicationList.as_view() ,name="application_list_class"),   
    url(r'^solicitud_nueva$', ApplicationCreate.as_view(),name="application_create"),
    url(r'^solicitud_editar/(?P<pk>\d+)/$', ApplicationUpdate.as_view(),name="application_edit"),
    url(r'^eliminar_solicitud/(?P<pk>\d+)/$', ApplicationDelete.as_view(),name="application_delete_class"), 


    url(r'^listado',listado, name="listado")


]