# Generated by Django 3.2.16 on 2022-11-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samcoApp', '0012_auto_20221120_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactu',
            old_name='url',
            new_name='facebook',
        ),
        migrations.AddField(
            model_name='contactu',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contactu',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contactu',
            name='tw',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contactu',
            name='whatApp',
            field=models.URLField(blank=True),
        ),
    ]
