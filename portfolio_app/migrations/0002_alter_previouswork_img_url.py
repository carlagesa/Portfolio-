# Generated by Django 4.0.4 on 2023-03-29 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previouswork',
            name='img_url',
            field=models.ImageField(default='static/assets/images/default.jpg', null=True, upload_to='static/assets/images'),
        ),
    ]