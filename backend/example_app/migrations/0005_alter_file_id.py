# Generated by Django 3.2.9 on 2022-08-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0004_auto_20220829_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]