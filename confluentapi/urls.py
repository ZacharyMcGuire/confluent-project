from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from confluentapi import views


urlpatterns = format_suffix_patterns([
    path('', views.api_root, name='root'),
    path('auth/', include('rest_framework.urls'), name='auth'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('pages/', views.PageList.as_view(), name='page-list'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='page-detail'),
    path('pages/<int:pk>/html/', views.PageHTML.as_view(), name='page-html'),
])
