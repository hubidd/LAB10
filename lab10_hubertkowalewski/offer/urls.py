from django.urls import path
from . import views

urlpatterns = [
    path('', views.kategorie_list, name='kategorie_list'),
    path('<int:kategoria_id>/', views.szkolenia_list, name='szkolenia_list'),
    path('categories/', views.api_categories, name='api_categories'),
    path('courses/', views.api_courses, name='api_courses'),
    path('search/', views.wyszukiwarka_szkolen, name='wyszukiwarka'),
]