# Generated by Django 4.0 on 2021-12-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tag_article_category_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
