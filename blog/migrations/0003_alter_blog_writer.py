# Generated by Django 3.2.6 on 2021-08-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_checks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='writer',
            field=models.CharField(max_length=200),
        ),
    ]
