from django.urls import path

from apps.posts import views

urlpatterns = [
    path('', views.view_all_posts),

]
