# Generated by Django 4.0.2 on 2022-02-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_imovei_garagem_alter_imovei_codigo_imovel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovei',
            name='banheiros',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
