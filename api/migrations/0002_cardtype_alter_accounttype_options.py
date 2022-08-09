# Generated by Django 4.0.6 on 2022-08-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CC', 'Credit Card'), ('DC', 'Debit Card')], max_length=100)),
                ('brand', models.CharField(choices=[('VISA', 'VISA'), ('MC', 'MasterCard')], max_length=100)),
                ('plan', models.CharField(choices=[('B', 'Basic'), ('E', 'Essential'), ('S', 'Silver'), ('G', 'Gold'), ('P', 'Platinum'), ('X', 'Executive')], max_length=100)),
                ('monthly_allowance', models.FloatField()),
                ('yearly_maintenance', models.FloatField()),
                ('description', models.TextField()),
                ('required_assets', models.FloatField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='accounttype',
            options={'ordering': ['id']},
        ),
    ]
