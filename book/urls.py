from . import views
from django.urls import path


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
        '<pk>/delete_comment/', views.DeleteComment.as_view(),
        name='delete'
    ),
    path(
        '<pk>/delete_comment/post/', views.ChapterDetail.as_view(),
        name='delete/reverse'
    ),
    path(
        '<pk>/update_comment/', views.UpdateComment.as_view(),
        name='update'
    ),
]
