"""my_project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include
from my_app import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FirmGenericViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', views.FirmGenericViewSet.as_view({
        'get': 'retrieve',
        'put': 'create',
        'delete': 'delete',
    })),
    path('create/', views.CategoryCreateAPIView.as_view()),
    path('', views.CategoryListAPIView.as_view()),
    path('update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    path('retrieve/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
]
