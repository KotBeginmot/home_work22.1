# Generated by Django 4.2.4 on 2023-08-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogrecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='превью'),
        ),
    ]
