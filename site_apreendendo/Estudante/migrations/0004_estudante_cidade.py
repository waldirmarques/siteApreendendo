# Generated by Django 2.2.2 on 2019-06-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudante', '0003_auto_20190613_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='cidade',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]