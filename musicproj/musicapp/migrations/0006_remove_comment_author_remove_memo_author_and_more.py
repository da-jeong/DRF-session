# Generated by Django 4.0.4 on 2022-07-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_memo_box_alter_comment_author_alter_memo_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='memo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='memo',
            name='box',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(default='null', max_length=512),
        ),
        migrations.AddField(
            model_name='memo',
            name='memo_author',
            field=models.CharField(default='멋쟁이 사자', max_length=512),
        ),
    ]
