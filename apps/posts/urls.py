from django.urls import path, re_path
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.view_all_users_posts, name="list"),
    re_path(r'^(?P<id>[\w-]+)/$', views.view_all_posts, name="user_list"),
    re_path(r'^(?P<id>[\w-]+)/create/$', views.post_create, name="create"),
    re_path(r'^(?P<id>[\w-]+)/edit-post/(?P<slug>[\w-]+)',
            views.post_edit, name="edit_post"),
    re_path(r'^(?P<id>[\w-]+)/(?P<slug>[\w-]+)/$',
            views.post_detail, name="view_user_post"),
    re_path('/send-email/', views.send_email, name="send_email"),
]
