# Generated by Django 2.1.1 on 2018-09-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boj', '0008_auto_20180908_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
