# Generated by Django 3.2.16 on 2022-11-15 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samcoApp', '0004_author_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samcoApp.author'),
        ),
    ]