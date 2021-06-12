# Generated by Django 3.1.7 on 2021-05-08 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20210504_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
