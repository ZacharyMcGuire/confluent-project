from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from confluentapi import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pages', views.PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'), name='auth'),
    path('openapi/', get_schema_view(
        title="Confluent Project",
        description="API for a simple Confluence clone.",
        version="0.1.0",
        url='http://127.0.0.1:8000/api/',
        urlconf='confluentapi.urls'
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]
