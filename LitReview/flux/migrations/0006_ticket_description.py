# Generated by Django 3.2.7 on 2021-10-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0005_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, max_length=2048),
        ),
    ]
