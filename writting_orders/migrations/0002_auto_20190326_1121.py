# Generated by Django 2.1.7 on 2019-03-26 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writting_orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
