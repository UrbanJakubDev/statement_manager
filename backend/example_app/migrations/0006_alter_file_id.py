# Generated by Django 3.2.9 on 2022-08-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0005_alter_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]