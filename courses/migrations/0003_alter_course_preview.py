# Generated by Django 4.2.10 on 2024-04-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(default='default_courses.jpg', upload_to='course_preview'),
        ),
    ]
