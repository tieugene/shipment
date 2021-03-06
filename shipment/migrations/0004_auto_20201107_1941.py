# Generated by Django 3.1.2 on 2020-11-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0003_auto_20201106_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctype',
            options={'ordering': ('name',), 'verbose_name': 'Тип документа', 'verbose_name_plural': 'Типы документа'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('-pk',), 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='org',
            options={'ordering': ('name',), 'verbose_name': 'Потребитель', 'verbose_name_plural': 'Потребитель'},
        ),
        migrations.AlterModelOptions(
            name='shipper',
            options={'ordering': ('name',), 'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.AlterField(
            model_name='doctype',
            name='fullname',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='name',
            field=models.CharField(db_index=True, max_length=16, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='document',
            name='comments',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(db_index=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='document',
            name='doctype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctype_document', to='shipment.doctype', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='document',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_document', to='shipment.org', verbose_name='Потребитель'),
        ),
        migrations.AlterField(
            model_name='document',
            name='shipper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipper_document', to='shipment.shipper', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='org',
            name='fullname',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='org',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Короткое наименование'),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='name',
            field=models.CharField(db_index=True, max_length=16, unique=True, verbose_name='Наименование'),
        ),
    ]
