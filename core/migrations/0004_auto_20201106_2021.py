# Generated by Django 3.0.10 on 2020-11-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201023_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-pk',), 'verbose_name': 'Файл', 'verbose_name_plural': 'Files'},
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Name'),
        ),
    ]