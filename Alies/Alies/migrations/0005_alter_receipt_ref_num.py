# Generated by Django 4.2.4 on 2023-08-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alies', '0004_drink_noodle_receipt_wing_delete_drinks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(blank=True, default='6772499544', editable=False, max_length=10, unique=True),
        ),
    ]
