# Generated by Django 2.1.1 on 2018-09-19 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0004_auto_20180906_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('text', 'Text'), ('date', 'Date'), ('number', 'Number')], default='text', max_length=10)),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='risk',
            name='data',
        ),
        migrations.AddField(
            model_name='risk',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='risk',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='field',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk.Risk'),
        ),
    ]
