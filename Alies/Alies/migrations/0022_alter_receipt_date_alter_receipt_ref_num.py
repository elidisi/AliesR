# Generated by Django 4.2.4 on 2023-08-09 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alies', '0021_receipt_status_alter_receipt_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 10, 4, 58, 23, 252597)),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(default='1292475520', max_length=10, unique=True),
        ),
    ]
