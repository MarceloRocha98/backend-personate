# Generated by Django 3.1.3 on 2020-11-15 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_points_x_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='system_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_img', models.ImageField(upload_to='')),
                ('nome1', models.CharField(max_length=100)),
                ('nome2', models.CharField(max_length=100)),
                ('nome3', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'system_images',
            },
        ),
    ]
