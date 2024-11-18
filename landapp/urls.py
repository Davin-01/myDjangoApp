from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('create/', views.create_item, name='create_item'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/update/', views.update_item, name='update_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

