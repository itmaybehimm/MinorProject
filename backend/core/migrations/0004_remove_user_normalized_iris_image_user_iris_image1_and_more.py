# Generated by Django 5.0.3 on 2024-03-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_file_alter_user_normalized_iris_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='normalized_iris_image',
        ),
        migrations.AddField(
            model_name='user',
            name='iris_image1',
            field=models.ImageField(default=None, upload_to='iris/'),
        ),
        migrations.AddField(
            model_name='user',
            name='iris_image2',
            field=models.ImageField(default=None, upload_to='iris/'),
        ),
        migrations.AddField(
            model_name='user',
            name='iris_image3',
            field=models.ImageField(default=None, upload_to='iris/'),
        ),
    ]