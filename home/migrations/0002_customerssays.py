# Generated by Django 5.0.6 on 2024-07-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersSays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=110)),
                ('customer_location', models.CharField(max_length=100)),
                ('customer_image', models.ImageField(upload_to='customers/images/')),
                ('customer_message', models.TextField()),
            ],
        ),
    ]
