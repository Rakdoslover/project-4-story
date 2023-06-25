from . import views
from django.urls import path
from .views import DeleteComment


urlpatterns = [
    path("", views.ChapterList.as_view(), name="home"),
    path('<slug:slug>/', views.ChapterDetail.as_view(), name='chapter_detail'),
    path(
        '<slug:slug>/GET', views.ChapterDetail.as_view(),
        name='chapter_detail/GET'
    ),
    path(
        '<slug:slug>/POST', views.ChapterDetail.as_view(),
        name='chapter_detail/POST'
    ),
    path(
        'delete/<slug:slug>/', views.DeleteComment.as_view(),
        name='delete_comment'
    ),
]
