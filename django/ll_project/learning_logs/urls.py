"""Define padrões de URL para learning logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Página inicial
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
]