# Generated by Django 3.1.2 on 2020-12-06 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cerveza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidosModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pendiente'), ('C', 'En curso'), ('F', 'Finalizado')], max_length=1)),
                ('costo_total', models.IntegerField()),
                ('cantidad_botellas', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega', models.DateTimeField(null=True)),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='cerveza.cervezamodel')),
            ],
        ),
    ]
