# Generated by Django 4.1.1 on 2022-10-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_watches'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
