# Generated by Django 3.2.16 on 2022-11-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samcoApp', '0007_auto_20221115_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author_img',
            name='name',
        ),
    ]