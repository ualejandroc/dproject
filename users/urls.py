from django.conf.urls import url, include
from django.contrib import admin
from views  import UserRegistration

from views import index


urlpatterns = [
    url(r'^index$', index),
    url(r'^registro$',UserRegistration.as_view(), name="regristro" ),

]