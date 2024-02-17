# Generated by Django 5.0.1 on 2024-02-12 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='Assets/UserPhoto/')),
                ('user_proof', models.FileField(upload_to='Assets/UserProof/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
