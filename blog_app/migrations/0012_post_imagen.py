# Generated by Django 4.1 on 2023-02-03 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
