# Generated by Django 2.1.7 on 2019-05-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writting_orders', '0020_auto_20190502_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='process',
            field=models.CharField(choices=[(1, 'Processing1'), (2, 'Finished')], max_length=12, null=True),
        ),
    ]