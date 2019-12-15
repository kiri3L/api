from django.conf.urls import url
from django.urls import path
from .views import get_gate, get_uids, bind, unbind, index, add_new_gates

urlpatterns = [
    path('get_gate', get_gate),
    path('get_uids', get_uids),
    path('add_new_gates', add_new_gates),
    path('bind', bind),
    path('unbind', unbind),
   # path('sub', sub),
    path('', index),
]
