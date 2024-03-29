# Generated by Django 5.0.1 on 2024-02-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeiTest', '0006_systemdec_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='latitude',
            name='orientation',
            field=models.CharField(choices=[('N', 'Nord'), ('S', 'Sud')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='longitude',
            name='orientation',
            field=models.CharField(choices=[('E', 'Est'), ('O', 'Ouest')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='degre',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='fuseau',
            field=models.CharField(choices=[('GMT', 'GMT')], max_length=10),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='minute',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='latitude',
            name='seconde',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='degre',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='fuseau',
            field=models.CharField(choices=[('GMT', 'GMT')], max_length=10),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='minute',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='longitude',
            name='seconde',
            field=models.FloatField(),
        ),
    ]
