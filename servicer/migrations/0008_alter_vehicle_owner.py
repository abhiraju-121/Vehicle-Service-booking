# Generated by Django 5.0.4 on 2025-01-08 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicer', '0007_vehicle_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='servicer.customer'),
        ),
    ]
