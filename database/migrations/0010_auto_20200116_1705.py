# Generated by Django 3.0.1 on 2020-01-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20200116_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Earliest_priority',
            field=models.CharField(default='', editable=False, max_length=800, null=True),
        ),
    ]
