# Generated by Django 3.0.5 on 2020-04-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default='url', max_length=142),
            preserve_default=False,
        ),
    ]
