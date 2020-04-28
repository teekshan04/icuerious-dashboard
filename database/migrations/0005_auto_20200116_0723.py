# Generated by Django 3.0.1 on 2020-01-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200116_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Applicants',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='report',
            name='Country',
            field=models.CharField(default='', editable=False, max_length=500),
        ),
        migrations.AlterField(
            model_name='report',
            name='Earliest_priority',
            field=models.CharField(default='', editable=False, max_length=800),
        ),
        migrations.AlterField(
            model_name='report',
            name='Earliest_publication',
            field=models.CharField(default='', editable=False, max_length=400),
        ),
        migrations.AlterField(
            model_name='report',
            name='Family_number',
            field=models.CharField(default='', editable=False, max_length=800),
        ),
        migrations.AlterField(
            model_name='report',
            name='Inventors',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='report',
            name='Publication_number',
            field=models.CharField(default='', editable=False, max_length=400),
        ),
        migrations.AlterField(
            model_name='report',
            name='Title',
            field=models.CharField(max_length=400),
        ),
    ]
