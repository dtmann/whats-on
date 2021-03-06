# Generated by Django 3.0.7 on 2020-08-17 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200817_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('e_image', models.ImageField(blank=True, upload_to='main/static')),
                ('tags', models.TextField(null=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Business')),
            ],
        ),
    ]
