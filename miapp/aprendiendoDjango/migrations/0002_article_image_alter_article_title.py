# Generated by Django 4.0.2 on 2022-02-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprendiendoDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
