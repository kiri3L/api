from django.conf.urls import url
from django.urls import path
from .views import get_gate, get_uids, bind, unbind, index, sub, add_gates

urlpatterns = [
    path('get_gate/<str:uid>/', get_gate),
    path('get_uids/<str:gate>/', get_uids),
    path('bind/a=<str:gate>&b=<str:uid>', bind),
    path('unbind/a=<str:gate>&b=<str:uid>', unbind),
    path('add_gates/<str:gate>', add_gates),
   # path('sub', sub),
    path('', index),
]
