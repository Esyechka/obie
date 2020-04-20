# Generated by Django 2.2.12 on 2020-04-20 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carriersearch.Carrier')),
                ('policy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carriersearch.Policy')),
                ('state', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carriersearch.State')),
            ],
        ),
    ]
