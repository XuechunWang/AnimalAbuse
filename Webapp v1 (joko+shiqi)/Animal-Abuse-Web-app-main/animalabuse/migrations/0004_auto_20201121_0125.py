# Generated by Django 3.1.2 on 2020-11-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalabuse', '0003_auto_20201120_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalabuse',
            name='data_source',
            field=models.CharField(choices=[('Government Sourced Entries', 'Government Sourced Entries'), ('Publicly Entered Entries', 'Publicly Entered Entries')], max_length=120, null=True),
        ),
    ]