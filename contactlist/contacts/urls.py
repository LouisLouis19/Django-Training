from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('edit/<int:contact_id>/', views.contact_edit, name='contact_edit'),
    path('delete/<int:contact_id>/', views.contact_delete, name='contact_delete'),
]