# Generated by Django 5.0.6 on 2024-07-05 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.room'),
        ),
    ]
