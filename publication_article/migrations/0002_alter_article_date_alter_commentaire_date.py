# Generated by Django 5.0.1 on 2024-02-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]