from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import SimpleRouter
from .views import MemoViewSet, CommentViewSet

memo_router = SimpleRouter(trailing_slash=False)
memo_router.register('memos', MemoViewSet, basename='memo')

comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(memo_router.urls)),
    path('memos/<int:memo_id>/', include(comment_router.urls)),
]
