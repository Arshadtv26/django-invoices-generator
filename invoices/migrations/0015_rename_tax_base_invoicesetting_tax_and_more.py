# Generated by Django 4.1.5 on 2023-02-24 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_alter_client_zip_code_alter_company_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicesetting',
            old_name='tax_base',
            new_name='tax',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoicesetting'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='tax_base',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='tax_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total_products',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]