from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Memo(models.Model):
  title = models.CharField(max_length=512)
  singer = models.CharField(max_length=256)
  date = models.DateField(auto_now_add=True)
  likes = models.PositiveIntegerField(null=True)
  content = models.TextField()
  genre_choices = [
        ('발라드', '발라드'), ('댄스', '댄스'), ('록', '록'),
        ('OST', 'OST'), ('인디', '인디'), ('POP', 'POP'),
        ('클래식', '클래식'), ('재즈', '재즈'), ('KPOP', 'KPOP'),
        ('CCM', 'CCM'), ('힙합', '힙합'), ('블루스', '블루스'), 
    ]
  genre = models.CharField( 
        max_length=16, choices = genre_choices
    )
  author = models.CharField(default = "멋쟁이 사자", max_length=512)
  nickname = models.CharField(max_length=512, null=True)
  memo_id = models.IntegerField(null=True)

  def __str__(self):
    return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    memo = models.ForeignKey('musicapp.Memo', null=True, blank=True, on_delete=models.CASCADE, related_name='memo_comments')
    author = models.CharField(default = "null", max_length=512)
    nickname = models.CharField(max_length=512, null=True)
    comment_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.memo.pk)

