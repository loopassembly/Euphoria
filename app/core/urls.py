from django.urls import path
from core import views
urlpatterns = [
    path("hello-view/",views.HelloApiView.as_view(), name="hello")
]
