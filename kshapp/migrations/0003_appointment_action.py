# Generated by Django 3.2 on 2022-06-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kshapp', '0002_auto_20220605_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='action',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Done', 'Done')], max_length=200, null=True),
        ),
    ]
