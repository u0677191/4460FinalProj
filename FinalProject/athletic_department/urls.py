from django.urls import path
from . import views


urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    # Define other URLs for CRUD operations
]
