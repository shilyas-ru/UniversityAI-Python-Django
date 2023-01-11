# Generated by Django 4.1.5 on 2023-01-09 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0011_alter_articles_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, default=None, help_text='Рубрика, к которой относится статья', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_blog.categories'),
        ),
    ]