# Generated by Django 4.2.1 on 2023-05-26 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendees', models.PositiveIntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('contract', models.ForeignKey(limit_choices_to={'status': True}, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='contracts.contract')),
                ('event_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.status')),
                ('support_contact', models.ForeignKey(blank=True, limit_choices_to={'team': 'SUPPORT'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
