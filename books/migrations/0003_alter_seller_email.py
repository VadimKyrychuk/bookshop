# Generated by Django 3.2.7 on 2021-09-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210914_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
    ]
