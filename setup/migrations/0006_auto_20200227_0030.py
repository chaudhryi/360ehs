# Generated by Django 3.0.3 on 2020-02-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_source_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
