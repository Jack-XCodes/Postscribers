# Generated by Django 4.0.4 on 2022-06-01 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
