# Generated by Django 2.0.5 on 2018-08-23 14:11

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('text', models.TextField(null=True, verbose_name='text')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='link')),
            ],
            options={
                'verbose_name': 'News item',
                'verbose_name_plural': 'News items',
                'ordering': ('-date',),
            },
        ),
    ]