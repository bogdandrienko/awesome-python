# Generated by Django 4.1.4 on 2023-07-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_place',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(default='', max_length=255),
        ),
    ]