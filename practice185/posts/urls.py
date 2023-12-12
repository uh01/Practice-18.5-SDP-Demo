from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_post, name='add_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.detete_post, name='delete_post'),
]