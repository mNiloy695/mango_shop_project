# Generated by Django 5.0.7 on 2024-07-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_remove_addressmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='order_status',
            field=models.CharField(choices=[('pending', 'pending'), ('running', 'running'), ('Completed', 'completed'), ('cancelled', 'cancelled')], default='Pending', max_length=10),
        ),
    ]
