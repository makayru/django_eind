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
    path('addreadaction/', views.AddReadAction, name='addreadaction'),
    path('addreadaction/<int:pk>', views.EditReadAction, name='edit_readaction'),
    path('deletereadaction/<int:pk>', views.DeleteReadAction, name='delete_readaction'),
<<<<<<< Updated upstream
=======
    path('newsfeed', views.News_feed, name='newsfeed'),
>>>>>>> Stashed changes
    path('books/', views.AllBooks, name='books'),
    path('myreadactions/', views.MyReadActions, name='myreadactions'),
    path('unapprovedbooks/', views.UnapprovedBooks, name='unapprovedbooks'),
    path('approve/<int:book_id>/', views.Approve_book, name='approve_book'),
    path('change-password/', views.change_password, name='change_password'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]