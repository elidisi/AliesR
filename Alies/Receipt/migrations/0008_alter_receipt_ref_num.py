# Generated by Django 4.2.4 on 2023-08-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0007_alter_receipt_ref_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(blank=True, default='5085107791', editable=False, max_length=10, unique=True),
        ),
    ]
