# Generated by Django 4.1.3 on 2022-12-12 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.CharField(choices=[('politics', 'politics'), ('tech', 'tech'), ('religion', 'religion'), ('sport', 'sport'), ('other', 'other')], default='other', max_length=10),
        ),
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='story',
            name='post',
            field=models.TextField(max_length=5000),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]