# Generated by Django 2.2.28 on 2022-12-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addressyczsczxypo'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressyczsczxypo',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
