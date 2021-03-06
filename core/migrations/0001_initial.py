# Generated by Django 2.2.6 on 2020-10-19 14:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.my_upload_to, verbose_name='Файл')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='File name')),
                ('mime', models.CharField(db_index=True, max_length=255, verbose_name='MIME type')),
                ('ctime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created')),
                ('size', models.PositiveIntegerField(db_index=True, verbose_name='Size')),
                ('crc', models.UUIDField(db_index=True, verbose_name='CRC')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Files',
            },
        ),
    ]
