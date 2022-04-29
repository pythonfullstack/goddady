"""goddady URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

application_info = openapi.Info(
    title="example",
    default_version='1.0',
    description='This is an example',
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="support@example.com"),
)

internal_redoc_view = get_schema_view(
    application_info,
    public=True,
    authentication_classes=(rest_framework.authentication.SessionAuthentication,),
    permission_classes=(permissions.AllowAny if settings.DEBUG else permissions.IsAuthenticated,),
)

internal_swagger_api_view = get_schema_view(
    application_info,
    public=True,
    authentication_classes=(rest_framework.authentication.SessionAuthentication,),
    permission_classes=(permissions.AllowAny if settings.DEBUG else permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', internal_swagger_api_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', internal_redoc_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('emr.urls')),

    path('', lambda request: redirect('docs/'), name='home')
]
