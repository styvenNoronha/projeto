# Generated by Django 3.2.7 on 2021-11-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10)),
                ('voltagem', models.IntegerField()),
                ('corrente', models.IntegerField()),
                ('CV', models.IntegerField()),
                ('RPM', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('desc_Pro', models.TextField(max_length=1000)),
                ('desc_Solu', models.TextField(max_length=1000)),
                ('valor_servico', models.FloatField()),
                ('fk_codEletrista', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='funcionarios.funcao')),
                ('fk_codMotor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manu.motor')),
            ],
        ),
    ]
