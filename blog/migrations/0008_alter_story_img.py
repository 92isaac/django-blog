# Generated by Django 4.1.3 on 2022-12-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_story_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='img',
            field=models.ImageField(default='/media/default.png', upload_to='blogpost_img'),
        ),
    ]
