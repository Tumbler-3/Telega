# Generated by Django 4.1.4 on 2023-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0003_alter_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]