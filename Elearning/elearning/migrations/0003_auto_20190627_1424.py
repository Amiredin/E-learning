# Generated by Django 2.2.2 on 2019-06-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_auto_20190627_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
