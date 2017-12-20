# Generated by Django 2.0 on 2017-12-17 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_id', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='deposit_account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=2)),
                ('over_draft', models.DecimalField(decimal_places=2, max_digits=2)),
                ('on_hold', models.DecimalField(decimal_places=2, max_digits=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'deposit_account',
            },
        ),
        migrations.CreateModel(
            name='loan_account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=2)),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'loan_account',
            },
        ),
    ]