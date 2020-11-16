"""personateBackend URL Configuration

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
from django.urls import path, include
from core import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from core.views import UserViewSet,PersonViewSet, GamesCreatedViewSet, ChallangesViewSet, PointsXSystemViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'person',PersonViewSet)
router.register(r'GamesCreated',GamesCreatedViewSet)
router.register(r'Challanges',ChallangesViewSet)
router.register(r'rank',PointsXSystemViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('login/',views.login_user),
    path('logout/',views.logout_user)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
