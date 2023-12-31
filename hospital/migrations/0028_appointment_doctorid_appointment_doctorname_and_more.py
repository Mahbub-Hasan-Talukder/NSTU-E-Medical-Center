# Generated by Django 4.2.4 on 2023-09-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0027_remove_appointment_doctorid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
