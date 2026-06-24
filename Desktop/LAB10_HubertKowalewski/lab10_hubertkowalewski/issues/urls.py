from django.urls import path
from . import views

urlpatterns = [
    path('problemReport/', views.problem_report, name='problem_report'),
    
    path('problems/', views.api_problems, name='api_problems'),
]