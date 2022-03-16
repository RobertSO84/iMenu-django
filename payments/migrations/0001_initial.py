# Generated by Django 4.0.2 on 2022-03-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(choices=[('CARD', 'card'), ('CASH', 'cash')], max_length=255)),
                ('status_payment', models.CharField(choices=[('PENDING', 'pending'), ('PAID', 'paid')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
