from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_contacts, name='contacts'),
    path('accounts/login/', views.view_login, name='login'),
    path('accounts/logout/', views.view_logout, name='logout'),
    path('<int:id_contact>/detail/', views.view_detail, name='detail'),
    path('<int:id_contact>/delete/', views.view_delete, name='delete'),
    path('add_contact/', views.view_add_contact, name='add'),
    path('add_new_user', views.view_add_new_user, name='add_new_user'),
    path('search/', views.view_search, name='search')
]
