# Generated by Django 4.2.4 on 2023-08-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0027_alter_receipt_ref_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(default='7047623283', editable=False, max_length=10, unique=True),
        ),
    ]
