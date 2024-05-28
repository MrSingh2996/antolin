# Generated by Django 5.0.6 on 2024-05-28 21:15

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
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('customer_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('glue', models.FloatField()),
                ('water', models.FloatField()),
                ('roving', models.FloatField()),
                ('roller_temperature', models.FloatField()),
                ('tool_temp_top', models.FloatField()),
                ('tool_temp_middle', models.FloatField()),
                ('tool_temp_bottom', models.FloatField()),
                ('wjc_pressure', models.FloatField()),
                ('date', models.DateField()),
                ('shift', models.CharField(max_length=10)),
            ],
        ),
    ]