# Generated by Django 2.2.2 on 2019-06-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]