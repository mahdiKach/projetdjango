# Generated by Django 3.2.3 on 2021-05-19 20:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emballage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere', models.CharField(max_length=100)),
                ('couleur', models.CharField(choices=[('bl', 'blanc'), ('rg', 'rouge'), ('ble', 'bleur'), ('vr', 'vert'), ('muli', 'multicolore')], default='Transparent', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duree_garantie', models.CharField(max_length=100)),
                ('dateCde', models.DateField(default=datetime.date.today, null=True)),
                ('totalCde', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.produit')),
            ],
        ),
    ]
