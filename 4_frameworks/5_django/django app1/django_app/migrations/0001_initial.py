# Generated by Django 4.1.2 on 2022-11-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(blank=True, default=0, verbose_name='user')),
                ('title', models.CharField(blank=True, default='', max_length=300, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ('-user',),
            },
        ),
    ]