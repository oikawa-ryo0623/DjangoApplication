from django.urls import path
from . import views

app_name = 'ocero'

urlpatterns = [
    path('',views.index,name = 'index'),#通常
    path('change/',views.change,name = 'change'),#通常
    path('onceindex/',views.onceindex,name = 'onceindex'),
]