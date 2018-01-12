# Generated by Django 2.0 on 2018-01-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='img_src',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='filtered_image',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d/filtered'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d/origin'),
        ),
    ]
