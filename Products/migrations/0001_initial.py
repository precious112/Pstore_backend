# Generated by Django 3.2 on 2022-01-12 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_image', models.ImageField(upload_to='media')),
                ('item_price', models.CharField(max_length=100)),
                ('about_item', models.TextField()),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
            ],
        ),
    ]
