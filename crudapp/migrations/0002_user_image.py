# Generated by Django 4.0.5 on 2022-07-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
