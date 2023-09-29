from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    path("", PostListView.as_view() ,name="blog-home"),
    path("user/<str:username>/", UserPostListView.as_view() ,name="user-posts"),
    path("post/<int:pk>/",PostDetailView.as_view(),name="post-detail"),   # here pk is the primary key, of the post that we want to view
    path("post/<int:pk>/",PostDetailView.as_view(),name="post-detail"),   # here pk is the primary key, of the post that we want to view
    path("post/<int:pk>/delete/",PostDeleteView.as_view(),name="post-delete"),   #post - template : post_confirm_delete.html
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="post-update"), 
    path("post/new/",PostCreateView.as_view(),name="post-create"),
    path("about/",views.about,name="blog-about")
]


# template : <app> / <model>_<viewtype>.html -> blog/post_list.html .
