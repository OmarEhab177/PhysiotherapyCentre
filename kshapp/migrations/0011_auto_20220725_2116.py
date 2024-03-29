# Generated by Django 3.2 on 2022-07-25 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kshapp', '0010_auto_20220725_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_type',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kshapp.patienttype'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='patient',
            name='type_disability',
        ),
        migrations.AddField(
            model_name='patient',
            name='type_disability',
            field=models.ManyToManyField(to='kshapp.Disability'),
        ),
    ]
