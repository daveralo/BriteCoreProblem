# Generated by Django 2.1.1 on 2018-09-06 03:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0003_risk_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[]),
        ),
    ]
