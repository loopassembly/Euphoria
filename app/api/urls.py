from django.urls import include, path

from rest_framework import routers, views
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()
router.register('people', PersonViewSet)
router.register('species', SpeciesViewSet)

urlpatterns = [
   path('testapi/', include(router.urls)),
]