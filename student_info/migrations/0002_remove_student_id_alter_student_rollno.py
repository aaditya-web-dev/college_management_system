# Generated by Django 5.0.3 on 2024-09-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(primary_key='true', serialize=False),
        ),
    ]
