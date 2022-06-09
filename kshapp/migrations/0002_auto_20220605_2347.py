# Generated by Django 3.2 on 2022-06-05 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kshapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Parents_contact',
            new_name='parents_contact',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_join',
        ),
        migrations.AddField(
            model_name='patient',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='adress',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
