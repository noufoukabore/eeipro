# Generated by Django 5.0.1 on 2024-02-09 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeiTest', '0008_remove_latitude_orientation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemDeclenchement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eei',
            name='system_dec',
        ),
        migrations.AddField(
            model_name='eei',
            name='type_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eeiTest.typesystem'),
        ),
        migrations.AlterField(
            model_name='typesystem',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='typesystem',
            name='system_declenchement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eeiTest.systemdeclenchement'),
        ),
        migrations.DeleteModel(
            name='SystemDec',
        ),
    ]
