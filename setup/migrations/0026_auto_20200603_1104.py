# Generated by Django 3.0.3 on 2020-06-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0025_auto_20200602_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='rate_lcn',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rate_lcn',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
