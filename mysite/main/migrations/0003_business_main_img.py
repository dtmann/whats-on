# Generated by Django 3.0.3 on 2020-02-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_business_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='main_img',
            field=models.ImageField(default='null', upload_to='static/'),
            preserve_default=False,
        ),
    ]
