# Generated by Django 4.0.4 on 2022-07-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0009_remove_comment_comment_writer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.CharField(default='null', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='memo',
            name='writer',
            field=models.CharField(default='멋쟁이 사자', max_length=512, null=True),
        ),
    ]
