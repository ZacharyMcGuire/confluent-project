from django.urls import path
from confluentweb import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='web-login'),
    path('logout/', views.Logout.as_view(), name='web-logout'),
    path('pages/', views.PageList.as_view(), name='web-page-list'),
    path('pages/<int:pk>/', views.PageDetail.as_view(), name='web-page-detail'),
]
