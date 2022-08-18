# Generated by Django 4.1 on 2022-08-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitefinanceira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
            ],
        ),
        migrations.AlterField(
            model_name='beneficios',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='recursos',
            name='proposta',
            field=models.CharField(max_length=100, verbose_name='proposta'),
        ),
    ]