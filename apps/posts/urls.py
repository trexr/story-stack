from django.urls import path, re_path
from apps.posts import views

urlpatterns = [
    path('', views.view_all_posts),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail)
]
