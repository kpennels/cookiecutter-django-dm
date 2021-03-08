"""config URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
# from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView

# from django.urls import re_path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions


# schema_view = get_schema_view(
#     openapi.Info(
#         title="",
#         default_version='v1',
#         description="",
#     ),
#     public=False,
#     permission_classes=(permissions.IsAdminUser,),
# )

urlpatterns = [
    path('v1/', include(('apps.core.urls', 'core'), namespace='core')),
    path('v1/', include(('apps.{{ cookiecutter.app_name }}.urls',
                         'apps.{{ cookiecutter.app_name }}'), namespace='{{ cookiecutter.app_name }}')),
    path('accounts/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('admin/', admin.site.urls, name='admin'),
    # re_path(
    #     r'^swagger(?P<format>\.json|\.yaml)$',
    #     login_required(schema_view.without_ui(cache_timeout=0)),
    #     name='schema-json'
    # ),
    # path(
    #     'swagger/',
    #     login_required(schema_view.with_ui('swagger', cache_timeout=0)),
    #     name='schema-swagger-ui'
    # ),
    # path('api/auth/oauth/', include('rest_framework_social_oauth2.urls')),
]
