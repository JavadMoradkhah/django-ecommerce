# Generated by Django 4.2.2 on 2023-06-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='store.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_tags', to='store.tag')),
            ],
            options={
                'unique_together': {('product', 'tag')},
            },
        ),
    ]
