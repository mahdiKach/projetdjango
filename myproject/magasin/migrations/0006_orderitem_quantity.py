# Generated by Django 3.2.3 on 2021-05-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
