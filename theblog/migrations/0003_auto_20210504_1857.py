# Generated by Django 3.1.7 on 2021-05-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]
