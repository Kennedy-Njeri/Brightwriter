# Generated by Django 2.1.7 on 2019-05-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writting_orders', '0014_auto_20190502_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='process',
            field=models.CharField(choices=[('C', 'Processing'), ('Q', 'Finished')], default='C', max_length=1),
        ),
    ]
