from django.urls import path,include
from django.views.generic import base
from rest_framework.routers import DefaultRouter

from core import views
router = DefaultRouter()
router.register('hello-viewset' ,views.HelloViewSet,basename='hello-viewset')
router.register('profile', views.UserProfileViewset )
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path("hello-view/",views.HelloApiView.as_view(), name="hello"),
    path("login/", views.UserLoginApiView.as_view()),
    
    path("", include(router.urls))
]
