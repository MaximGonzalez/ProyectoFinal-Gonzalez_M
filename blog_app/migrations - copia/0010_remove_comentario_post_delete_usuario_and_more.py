# Generated by Django 4.1 on 2023-02-01 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_alter_post_contenido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
