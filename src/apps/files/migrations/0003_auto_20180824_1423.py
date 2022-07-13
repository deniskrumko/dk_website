# Generated by Django 2.0.5 on 2018-08-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='link_low',
            field=models.TextField(blank=True, null=True, verbose_name='Link (360p)'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='link',
            field=models.TextField(blank=True, null=True, verbose_name='Link (720p)'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='link_hd',
            field=models.TextField(blank=True, null=True, verbose_name='Link (1080p)'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='youtube_link',
            field=models.TextField(blank=True, null=True, verbose_name='Youtube code'),
        ),
    ]