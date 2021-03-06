# Generated by Django 3.0.6 on 2020-06-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('faculty', models.CharField(max_length=100)),
                ('batch', models.IntegerField(max_length=4)),
                ('college', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('tu_registraion_number', models.CharField(max_length=15)),
                ('semester', models.CharField(max_length=5)),
                ('terms_conditions', models.CharField(max_length=4)),
            ],
        ),
    ]
