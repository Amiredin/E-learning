# Generated by Django 2.2.2 on 2019-07-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_auto_20190629_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='category',
        ),
        migrations.AddField(
            model_name='exams',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exams',
            name='image',
            field=models.ImageField(upload_to='elearning/'),
        ),
    ]
