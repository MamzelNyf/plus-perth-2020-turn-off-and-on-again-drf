# Generated by Django 3.0.8 on 2020-11-13 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0005_organisation_slug'),
        ('listing', '0010_auto_20201110_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.Organisation'),
        ),
    ]
