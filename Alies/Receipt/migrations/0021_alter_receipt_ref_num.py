# Generated by Django 4.2.4 on 2023-08-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipt', '0020_currenttransaction_alter_receipt_ref_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(default='1591775701', editable=False, max_length=10, unique=True),
        ),
    ]