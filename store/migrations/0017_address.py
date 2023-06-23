# Generated by Django 4.2.2 on 2023-06-23 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0016_promotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_number', models.CharField(blank=True, max_length=20, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('is_default', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='store.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
