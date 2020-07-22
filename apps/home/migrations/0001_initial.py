# Generated by Django 2.2.11 on 2020-07-10 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='menu name')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Menu Link')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='menu icon')),
                ('status', models.CharField(choices=[('y', 'Show'), ('n', 'Hide')], default='y', max_length=1, verbose_name='Display status')),
            ],
            options={
                'verbose_name': 'Menu Bar',
                'verbose_name_plural': 'Menu Bar',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='leave me a message')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Webmaster')),
            ],
            options={
                'verbose_name': 'Website message',
                'verbose_name_plural': 'Website message',
            },
        ),
    ]
