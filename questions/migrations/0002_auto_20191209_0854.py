# Generated by Django 2.0 on 2019-12-09 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-likes']},
        ),
    ]
