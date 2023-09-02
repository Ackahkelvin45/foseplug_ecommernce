# Generated by Django 4.2.4 on 2023-08-31 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_alter_cartiten_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartiten',
            name='listing',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_item', to='listing.listing'),
        ),
        migrations.AlterField(
            model_name='cartiten',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
