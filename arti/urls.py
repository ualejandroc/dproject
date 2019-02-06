from django.conf.urls import url, include
from django.contrib import admin
from views import index  #, custommer_View, lista, 
    

from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^index/$', index),
    #url(r'^nuevo$', login_required( custommer_View ),name="custommer_create"),
    # url(r'^nuevo$', CustommerCreate.as_view(),name="custommer_create"),
    # url(r'^lista$', lista,name="custommer_list"),
]
    