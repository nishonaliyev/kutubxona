from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from kitoblar import views
from .views import CustomUserVIew, CommentVIew, LikeViewSet, BOokVIewSet, get_like, get_comment

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserVIew)
router.register(r'comment', views.CommentVIew)
router.register(r'book', views.BOokVIewSet)
router.register(r'like', views.LikeViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('like-count/<int:book_id>/', get_like, name='like-count'),
    path('comment-get/', get_comment, name='comment-count'),
]