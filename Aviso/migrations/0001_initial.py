# Generated by Django 4.0.5 on 2022-06-23 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula_avi', models.IntegerField(max_length=100)),
                ('Assunto_avi', models.CharField(max_length=100)),
                ('Data_avi', models.DateField(max_length=100)),
            ],
        ),
    ]
