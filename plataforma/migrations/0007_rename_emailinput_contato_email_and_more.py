# Generated by Django 4.0.2 on 2022-03-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_contato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='emailinput',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='mensagemInput',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='contato',
            old_name='nameInput',
            new_name='name',
        ),
    ]
