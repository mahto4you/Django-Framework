# Generated by Django 3.0.6 on 2020-11-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
        migrations.AddField(
            model_name='student',
            name='comment2',
            field=models.CharField(default='available', max_length=40),
        ),
    ]
