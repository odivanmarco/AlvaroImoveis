# Generated by Django 4.0.2 on 2022-03-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_contato_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovei',
            name='bairro',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
