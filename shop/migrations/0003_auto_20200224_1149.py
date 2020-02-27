# Generated by Django 3.0.3 on 2020-02-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200219_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='battery',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='colors',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='cpu',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='front_camera',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='main_camera',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='operating_system',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='ram',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='screen',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='phone',
            name='storage',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]