from .models import Memo, Comment
#from users.serializers import UserSerializer
from rest_framework import serializers

class MemoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Memo
        fields = [
            'title', 'singer', 'date', 'likes',
            'content', 'genre', 'nickname', 'memo_id'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'date', 'memo', 'nickname', 'comment_id']