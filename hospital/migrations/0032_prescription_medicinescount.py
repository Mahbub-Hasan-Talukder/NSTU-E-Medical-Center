# Generated by Django 4.2.5 on 2023-09-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0031_remove_chat_recipient_remove_chat_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='medicinesCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
