# Generated by Django 5.0.1 on 2024-02-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeiTest', '0007_latitude_orientation_longitude_orientation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latitude',
            name='orientation',
        ),
        migrations.RemoveField(
            model_name='longitude',
            name='orientation',
        ),
        migrations.AlterField(
            model_name='latitude',
            name='degre',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='fuseau',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='minute',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='seconde',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='degre',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='fuseau',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='minute',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='seconde',
            field=models.IntegerField(),
        ),
    ]
