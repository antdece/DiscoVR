# Generated by Django 2.0.6 on 2018-06-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20180625_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumb',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
