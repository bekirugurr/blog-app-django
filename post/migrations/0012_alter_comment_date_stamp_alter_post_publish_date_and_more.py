# Generated by Django 4.0.4 on 2022-06-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_postview_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
