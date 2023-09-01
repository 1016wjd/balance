from django.urls import path
from . import views


app_name = 'polls'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/comments/', views.comment, name='comment'),
   
]