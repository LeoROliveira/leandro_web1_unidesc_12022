# Generated by Django 4.0.5 on 2022-06-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pag', models.CharField(max_length=100)),
                ('data_pag', models.DateField(max_length=100)),
                ('banco_pag', models.CharField(max_length=100)),
                ('agencia_pag', models.CharField(max_length=100)),
                ('conta_pag', models.CharField(max_length=100)),
            ],
        ),
    ]