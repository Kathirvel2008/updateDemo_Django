"""updateDemo URL Configuration

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
from updateApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page , name="Login"),
    path('details/', views.details_page , name="Details"),
    path('list/', views.list_page , name="List"),
    path('delete/<id>', views.delete_page , name="Delete"),
    path('update/<id>', views.update_page , name="Update"),
]
