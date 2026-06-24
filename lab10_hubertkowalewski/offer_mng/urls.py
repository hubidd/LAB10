from django.urls import path
from . import views

urlpatterns = [
    path('categ-add/', views.categ_add, name='categ_add'),
    path('course-add/', views.course_add, name='course_add'),
]