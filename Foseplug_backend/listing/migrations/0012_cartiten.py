# Generated by Django 4.2.4 on 2023-08-30 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0011_alter_listing_category_alter_listing_store_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartIten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.ImageField(blank=True, null=True, upload_to='')),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_item', to='listing.listing')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
