# Generated by Django 3.0 on 2019-12-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField(default=1)),
                ('email', models.CharField(max_length=50)),
                ('texto_blod', models.CharField(max_length=150)),
                ('tema', models.CharField(choices=[('ROM', 'Romance'), ('GAM', 'Games'), ('PRO', 'Profissão')], max_length=3)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
