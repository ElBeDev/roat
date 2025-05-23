# Generated by Django 5.2 on 2025-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_payment_date_order_payment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('created', 'Creado'), ('processing', 'Procesando'), ('shipped', 'Enviado'), ('delivered', 'Entregado'), ('cancelled', 'Cancelado')], default='created', max_length=20, verbose_name='Estado del Pedido'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_reference',
            field=models.CharField(blank=True, max_length=100, verbose_name='Referencia de Pago'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_company',
            field=models.CharField(blank=True, max_length=100, verbose_name='Empresa de Envío'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_tracking_code',
            field=models.CharField(blank=True, max_length=100, verbose_name='Código de Seguimiento'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_tracking_url',
            field=models.URLField(blank=True, verbose_name='URL de Seguimiento'),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='ID de Transacción'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='ID de Pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Tarjeta de crédito/débito'), ('oxxo', 'OXXO'), ('transfer', 'Transferencia bancaria')], default='card', max_length=20, verbose_name='Método de Pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('processing', 'Procesando'), ('paid', 'Pagado'), ('failed', 'Fallido'), ('refunded', 'Reembolsado')], default='pending', max_length=20, verbose_name='Estado de Pago'),
        ),
    ]
