from django.urls import path
from . import views


app_name = 'polls'


urlpatterns = [
    path('', views.index, name='index'),
    # path('game/', views.game, name='game'),
    path('<int:poll_id>/game', views.game, name='game'),
    path('<int:poll_id>/comments/', views.comment, name='comment'),
    
   
]