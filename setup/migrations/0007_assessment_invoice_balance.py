# Generated by Django 3.0.3 on 2020-02-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_auto_20200227_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='invoice_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
