# Generated by Django 3.2.11 on 2022-01-31 18:03

import django.db.models.deletion
from django.db import migrations, models

import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200920_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(db_index=True, max_length=64, null=True, unique=True, verbose_name='Slug')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Blog category',
                'verbose_name_plural': 'Blog categories',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='blogentry',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogs', to='blog.blogcategory', verbose_name='Category'),
        ),
    ]