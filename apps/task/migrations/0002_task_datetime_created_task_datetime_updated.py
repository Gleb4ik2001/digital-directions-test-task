# Generated by Django 5.2.1 on 2025-06-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datetime_created',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата создания задачи'),
        ),
        migrations.AddField(
            model_name='task',
            name='datetime_updated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата обновления задачи'),
        ),
    ]
