"""
URL configuration for FinalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from athletic_department import views, urls as athletic_urls
from django.views import View
from athletic_department.views import AthleteListView, EmployeeListView



#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('athletic_department/teams/', views.team_list, name='team_list'),
#    path('athletic_department/homepage/', views.homepage, name='homepage'),

#]

#from django.urls import path
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('homepage/', views.homepage, name='homepage'),
    #path('teams/', include('athletic_department.urls')),  # Add this line to include the team-related URLs
    path('athletes', AthleteListView.as_view(), name='athlete_list'),  # Add this line
    path('', include('athletic_department.urls')), 
    path('employees/', include((athletic_urls.urlpatterns, 'athletic_department'), namespace='employees')),
    #path('employees/', include('athletic_department.urls', namespace='athletic_department')),

    # Define other URLs for CRUD operation
]
