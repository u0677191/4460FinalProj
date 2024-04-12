from django.urls import path
from . import views
from .views import TeamCreateView


urlpatterns = [
    path('teams/', views.team_list, name='team_list'),

    path('teams/create/', TeamCreateView.as_view(), name='team_create'),


    path('homepage/', views.homepage, name='homepage'),
    #path('add_employee/', views.add_employee, name='add_employee'),

    # Define other URLs for CRUD operation
]


