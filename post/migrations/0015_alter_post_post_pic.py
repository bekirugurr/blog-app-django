# Generated by Django 4.0.4 on 2022-06-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_remove_postview_time_tamp_postview_who_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
    ]