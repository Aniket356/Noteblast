# Generated by Django 4.1 on 2022-10-19 14:47

import accounts.manager
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_user_grade'),
        ('core', '0009_alter_post_posted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', accounts.manager.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
