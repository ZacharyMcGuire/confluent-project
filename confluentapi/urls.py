from django.urls import path, include
from rest_framework.routers import DefaultRouter
from confluentapi import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pages', views.PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='auth'),
]
