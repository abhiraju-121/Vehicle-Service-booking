# Generated by Django 5.0.4 on 2025-01-09 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicer', '0016_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='owner',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='servicer.customer'),
        ),
    ]
