# Generated by Django 4.0.6 on 2022-08-13 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_card_cvv'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedDepositPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('miminum_amount', models.FloatField()),
                ('mimimum_term_in_year', models.FloatField()),
                ('maximum_term_in_year', models.FloatField()),
                ('intrest_per_anum', models.FloatField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('time_of_withdraw', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('time_of_transaction', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('receiver_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to='api.account')),
                ('sender_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to='api.account')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FixedDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('time_of_initiation', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fixeddepositplan')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('time_of_deposit', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
