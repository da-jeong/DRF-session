from django.shortcuts import render
from django.views import View
from .models import Memo, Comment
from .serializer import MemoSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class MemoViewSet(ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, **kwargs):
        memo_id = self.kwargs['memo_id']
        return self.queryset.filter(memo = memo_id)



