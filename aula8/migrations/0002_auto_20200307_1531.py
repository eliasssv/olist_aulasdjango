# Generated by Django 3.0.3 on 2020-03-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula8', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name': 'Animau', 'verbose_name_plural': 'Animaus'},
        ),
        migrations.AddField(
            model_name='pet',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
