# Generated by Django 4.0.4 on 2022-07-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0012_remove_comment_writer_remove_memo_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='box',
            field=models.CharField(default='멋쟁이', max_length=512),
        ),
        migrations.AlterField(
            model_name='memo',
            name='box',
            field=models.CharField(default='멋쟁이', max_length=512, null=True),
        ),
    ]
