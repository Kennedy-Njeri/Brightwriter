# Generated by Django 2.1.7 on 2019-05-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writting_orders', '0025_auto_20190502_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='order',
            name='process',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Finished', 'Finished')], default='Processing', max_length=12),
        ),
    ]
