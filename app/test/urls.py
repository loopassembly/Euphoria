from django.urls import include, path

from rest_framework import routers, views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import obtain_auth_token
from .views import UserViewSet,MenuViewSet,UserLoginApiView

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('Menu', MenuViewSet)
# router.register('Menu', UserLoginApiView)


urlpatterns = [
   path('', include(router.urls)),
   path("login/", UserLoginApiView.as_view())
]