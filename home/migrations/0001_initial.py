# Generated by Django 5.0.6 on 2024-07-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.ImageField(upload_to='service/images/')),
                ('service_title', models.CharField(max_length=75)),
                ('service_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SliderServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=200)),
                ('slider_description', models.TextField()),
                ('slider_image', models.ImageField(upload_to='slider/images/')),
                ('slider_button', models.CharField(max_length=45)),
                ('slider_button_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
