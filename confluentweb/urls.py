from django.urls import path
from confluentweb import views


urlpatterns = [
    path('', views.index, name='web-index'),
    path('login/', views.Login.as_view(), name='web-login'),
    path('logout/', views.Logout.as_view(), name='web-logout'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='web-page-detail'),
]
