# Generated by Django 3.2.6 on 2022-01-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
