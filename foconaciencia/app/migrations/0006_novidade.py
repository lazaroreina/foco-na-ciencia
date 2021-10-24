# Generated by Django 3.2.8 on 2021-10-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_palavras_chave_questao_palavraschave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='')),
                ('links', models.CharField(max_length=30)),
            ],
        ),
    ]
