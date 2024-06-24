# Generated by Django 5.0.6 on 2024-06-21 17:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msproduct', '0002_alter_bill_id_alter_color_id_alter_image_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='color',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='price',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47235bc7-b13a-4020-982d-d9d8f9b7a4b7'), primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]