# Generated by Django 4.1.5 on 2023-01-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0006_alter_articles_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(blank=True, help_text='URL для указанного тэга (должен быть уникальным)', max_length=250, null=True, unique=True),
        ),
    ]
