# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-12 20:29
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default=b'Undefined', null=True)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('image', models.ImageField(blank=True, default=b'static/packet_images/no_image.png', null=True, upload_to=b'static/packet_images/')),
                ('type', models.TextField(default=b'Type of packet', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PacketCatalog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default=b'Packet Catalog', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PacketState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default=b'Undefined', null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivatedPacket',
            fields=[
                ('packetstate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='packet.PacketState')),
            ],
            bases=('packet.packetstate',),
        ),
        migrations.CreateModel(
            name='CustomPacket',
            fields=[
                ('packet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='packet.Packet')),
                ('startDate', models.DateTimeField(null=True)),
                ('endDate', models.DateTimeField(null=True)),
            ],
            bases=('packet.packet',),
        ),
        migrations.CreateModel(
            name='DeactivatedPacket',
            fields=[
                ('packetstate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='packet.PacketState')),
            ],
            bases=('packet.packetstate',),
        ),
        migrations.CreateModel(
            name='IncompletePacket',
            fields=[
                ('packetstate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='packet.PacketState')),
            ],
            bases=('packet.packetstate',),
        ),
        migrations.CreateModel(
            name='StandardPacket',
            fields=[
                ('packet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='packet.Packet')),
                ('durate', models.IntegerField(default=30)),
                ('expiringDate', models.DateTimeField()),
            ],
            bases=('packet.packet',),
        ),
        migrations.AddField(
            model_name='packet',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='courses', to='course.Course'),
        ),
        migrations.AddField(
            model_name='packet',
            name='packetcatalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packets', to='packet.PacketCatalog'),
        ),
        migrations.AddField(
            model_name='packet',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packets', to='packet.PacketState', to_field=b'name'),
        ),
    ]
