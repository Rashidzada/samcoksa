# Generated by Django 3.2.16 on 2022-11-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samcoApp', '0010_auto_20221115_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
