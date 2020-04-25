from django.urls import path, re_path
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.view_all_posts, name="list"),
    re_path(r'^create/$', views.post_create, name="create"),
    re_path(r'^edit-post/(?P<slug>[\w-]+)', views.post_edit, name="edit_post"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail),
]
