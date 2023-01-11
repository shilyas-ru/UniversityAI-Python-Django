# Generated by Django 4.1.5 on 2023-01-06 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0003_alter_articles_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(default=None, help_text='Автор статьи', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, default=None, help_text='Рубрика, к которой относится статья', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_blog.categories'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tag',
            field=models.ManyToManyField(blank=True, default=None, help_text='Тэги, связанные со статьёй', to='app_blog.tags'),
        ),
    ]
