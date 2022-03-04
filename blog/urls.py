from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('speakers/', views.speakers_list_view, name='list'),
]