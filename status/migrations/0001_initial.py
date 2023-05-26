# Generated by Django 4.2.1 on 2023-05-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PENDING', 'PENDING'), ('SIGNED', 'SIGNED'), ('CREATED', 'CREATED'), ('CANCELLED', 'CANCELLED'), ('POSTPONED', 'POSTPONED'), ('COMPLETE', 'COMPLETE')], default='CREATED', max_length=20)),
            ],
        ),
    ]
