from . import views
from django.urls import path

urlpatterns = [
    path("", views.ChapterList.as_view(), name="home"),
]
