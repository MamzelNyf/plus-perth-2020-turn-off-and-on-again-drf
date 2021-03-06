# Generated by Django 3.0.8 on 2020-11-10 13:39

from django.db import migrations, models
import listing.models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_auto_20201109_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='audience',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listing.models.upload_image_to),
        ),
        migrations.AddField(
            model_name='level',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listing.models.upload_image_to),
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listing.models.upload_image_to),
        ),
        migrations.AddField(
            model_name='type',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listing.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listing.models.upload_image_to),
        ),
    ]
