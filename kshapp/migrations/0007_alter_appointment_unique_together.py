# Generated by Django 3.2 on 2022-07-23 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kshapp', '0006_alter_patient_uplode'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('date', 'time', 'therapist'), ('date', 'time', 'patient')},
        ),
    ]
