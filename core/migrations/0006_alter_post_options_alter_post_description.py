# Generated by Django 4.1 on 2022-10-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_date_posted_post_posted_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=1500),
        ),
    ]
