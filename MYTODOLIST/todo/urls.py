from django.urls import path, include
from . import views

urlpatterns = [
path('home/', views.index, name='index'),
path('s\'inscrire/', views.register, name='register'),
path('todolist/',views.list,name='list'),
path('supprimer/<int:tache_id>/',views.delete,name='delete'),
path('modifier/<int:tache_id>/', views.modifier, name='modifier'),

]