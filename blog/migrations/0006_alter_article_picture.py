# Generated by Django 4.0 on 2021-12-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to='articles'),
        ),
    ]
