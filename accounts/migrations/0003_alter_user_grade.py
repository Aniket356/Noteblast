# Generated by Django 4.1 on 2022-11-09 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
    ]
