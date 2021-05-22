"""videoclubgarven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from myapp import views, users, movies

admin.site.site_header = "Garven Admin"

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('admin/users/', users.index, name='users'),
    path('admin/users/<int:user_id>/', users.deleteUser, name='deleteUser'),
    path('admin/movies/', movies.index, name='movies'),

    path('adminDjango', admin.site.urls, name='admin')
]


