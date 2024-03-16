# Generated by Django 5.0.1 on 2024-03-16 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('supplier_name', models.CharField(max_length=50)),
                ('supplier_email', models.CharField(max_length=100)),
                ('supplier_phone', models.CharField(max_length=15)),
                ('supplier_address', models.CharField(max_length=50)),
                ('supplier_city', models.CharField(max_length=50)),
                ('supplier_country', models.CharField(max_length=50)),
                ('supplier_postcode', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Exclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mandatory', models.CharField(choices=[('Theft', 'Theft'), ('Fraud', 'Fraud'), ('Bribery', 'Bribery'), ('None', 'None')], max_length=50)),
                ('discretionary', models.CharField(choices=[('Bankruptcy', 'Bankruptcy'), ('Improper Procurement', 'Improper Procurement'), ('Breach of Contract', 'Breach of Contract'), ('None', 'None')], max_length=50)),
                ('exclusion_date', models.DateField(blank=True, null=True)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_type', models.CharField(choices=[('Agricultural', 'Agricultural'), ('Automotive', 'Automotive'), ('Clothing & Accessories', 'Clothing & Accessories'), ('Construction Materials', 'Construction Materials'), ('Education & Training', 'Education & Training'), ('Financial Services', 'Financial Services'), ('Hospitality, Food & Beverage', 'Hospitality, Food & Beverage'), ('IT Services', 'IT Services'), ('Medical Equipment', 'Medical Equipment'), ('Office Supplies', 'Office Supplies')], max_length=50)),
                ('legal_form', models.CharField(choices=[('Sole Trader', 'Sole Trader'), ('Limited Company', 'Limited Company'), ('Charity', 'Charity')], max_length=50)),
                ('vat_no', models.CharField(max_length=20)),
                ('supplier_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.supplier')),
            ],
        ),
    ]
