# Generated by Django 4.0 on 2021-12-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
