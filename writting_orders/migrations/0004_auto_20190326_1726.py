# Generated by Django 2.1.7 on 2019-03-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writting_orders', '0003_auto_20190326_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='attach',
            new_name='pdf',
        ),
    ]
