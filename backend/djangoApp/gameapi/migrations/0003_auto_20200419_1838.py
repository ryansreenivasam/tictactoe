# Generated by Django 3.0.5 on 2020-04-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapi', '0002_auto_20200419_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='board',
            field=models.CharField(default='         ', max_length=9),
        ),
    ]