# Generated by Django 5.0.2 on 2024-12-20 13:11

import django.contrib.postgres.indexes
import django.db.models.deletion
import uuid
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('opened', 'Open'), ('closed', 'Closed')], default='opened', max_length=10, verbose_name='Status')),
                ('session_key', models.CharField(blank=True, max_length=255, verbose_name='Session key')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Total quantity')),
                ('total_price', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=20, verbose_name='Total price')),
                ('parameters', models.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('object_id', models.CharField(help_text='Please enter the ID of the related object.', max_length=255, verbose_name='Object ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('parameters', models.JSONField(blank=True, default=dict)),
                ('content_type', models.ForeignKey(help_text='Please select the type (model) for the relation, you want to build.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name="Related object's type (model)")),
            ],
            options={
                'verbose_name': 'Cart item',
                'verbose_name_plural': 'Cart items',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Price')),
                ('parameters', models.JSONField(blank=True, default=dict)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='ok_cart.cart', verbose_name='Cart')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='ok_cart.cartitem', verbose_name='Base item')),
                ('relations', models.ManyToManyField(blank=True, related_name='related_groups', to='ok_cart.cartitem', verbose_name='Related items')),
            ],
            options={
                'verbose_name': 'Cart group',
                'verbose_name_plural': 'Cart groups',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='cart',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created_at'], name='ok_cart_car_created_4e00bf_brin'),
        ),
        migrations.AddIndex(
            model_name='cartitem',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created_at'], name='ok_cart_car_created_7e499f_brin'),
        ),
        migrations.AddIndex(
            model_name='cartgroup',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created_at'], name='ok_cart_car_created_b660cf_brin'),
        ),
    ]
