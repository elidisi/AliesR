# Generated by Django 4.2.4 on 2023-08-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alies', '0019_alter_receipt_ref_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='items',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='ref_num',
            field=models.CharField(default='4819507081', editable=False, max_length=10, null=True, unique=True),
        ),
    ]