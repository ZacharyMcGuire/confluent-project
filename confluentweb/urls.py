from django.urls import path
from confluentweb import views


urlpatterns = [
    path('pages/', views.PageList.as_view(), name='page-list'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='page-detail'),
]
