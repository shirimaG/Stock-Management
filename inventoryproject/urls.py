"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from stockmgt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list_items, name='list_items'),
    path('add/',views.add_items, name ='add_items'),
    path('update/<str:pk>/',views.update_items, name ='update_items'),
    path('delete/<str:pk>/',views.delete_items, name ='delete_items'),
    path('details/<str:pk>/',views.stock_details, name ='stock_details'),
    path('issue/<str:pk>/',views.issue_items, name ='issue_items'),
    path('receive/<str:pk>/',views.receive_items, name ='receive_items'),
    path('reorder/<str:pk>/',views.reorder_level, name ='reorder_level'),
    path('admin/', admin.site.urls),
]
