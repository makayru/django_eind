"""django_eindopdracht URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("", include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('myprofile/', views.MyProfile, name='myprofile'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
    path('my_profile/<int:pk>/', views.edit_profile, name='my_profile'),
    path('addnewbook/', views.AddNewBooks, name='addnewbook'),
    path('books/', views.AllBooks, name='books'),

]