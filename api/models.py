from django.db import models


class AccountType(models.Model):
    name = models.CharField(max_length=100)
    yearly_intrest_rate = models.FloatField()
    minimum_balance = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Account(models.Model):
    number = models.CharField(max_length=16)
    ifsc = models.CharField(max_length=16)
    balance = models.FloatField()
    holder_name = models.CharField(max_length=200)
    holder_email = models.CharField(max_length=200)
    holder_phone = models.CharField(max_length=15)
    holder_phone = models.CharField(max_length=15)
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.number}  -  {self.holder_name}'


