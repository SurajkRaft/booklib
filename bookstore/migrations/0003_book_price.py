# Generated by Django 3.1 on 2022-08-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]