# Generated by Django 4.2.10 on 2024-04-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
