# Generated by Django 3.2 on 2022-07-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kshapp', '0007_auto_20220725_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='nationality',
            field=models.CharField(choices=[('Kuwaiti', 'Kuwaiti'), ('Egyption', 'Egyption'), ('Iraqi', 'Iraqi'), ('Jordanian', 'Jordanian'), ('Non-Kuwaiti', 'Non-Kuwaiti'), ('Saudi', 'Saudi'), ('Syrian', 'Syrian'), ('Yemeni', 'Yemeni'), ('Indian', 'Indian')], max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='parents_contact',
            field=models.CharField(max_length=200),
        ),
    ]
