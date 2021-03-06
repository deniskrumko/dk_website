# Generated by Django 2.0.5 on 2018-10-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20181015_1826'),
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryentry',
            name='done',
            field=models.BooleanField(default=False, verbose_name='done'),
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='diary_entries', to='files.File', verbose_name='files'),
        ),
    ]
