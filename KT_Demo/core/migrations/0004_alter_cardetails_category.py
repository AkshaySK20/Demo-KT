# Generated by Django 5.0.7 on 2024-07-20 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cardetails_options_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetails',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.category'),
        ),
    ]
