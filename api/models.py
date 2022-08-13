from random import choices
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


class CardType(models.Model):
    type = models.CharField(max_length=100, choices=[
        ('CC', "Credit Card"),
        ('DC', "Debit Card"),
    ])
    brand = models.CharField(max_length=100, choices=[
        ('VISA', "VISA"),
        ('MC', "MasterCard"),
    ])
    plan = models.CharField(max_length=100, choices=[
        ('B', "Basic"),
        ('E', "Essential"),
        ('S', "Silver"),
        ('G', "Gold"),
        ('P', "Platinum"),
        ('X', "Executive"),
    ])
    monthly_allowance = models.FloatField()
    yearly_maintenance = models.FloatField()
    description = models.TextField()
    required_assets = models.FloatField()
    overdue_monthly_intrest_rate = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        matrix = {
            'CC': "Credit Card",
            'DC': "Debit Card",
            'VISA': "VISA",
            'MC': "MasterCard",
            'B': "Basic",
            'E': "Essential",
            'S': "Silver",
            'G': "Gold",
            'P': "Platinum",
            'X': "Executive",
        }
        return f'{matrix[self.type]} - {matrix[self.brand]} - {matrix[self.plan]} | Monthly: {self.monthly_allowance}'


class Card(models.Model):
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    card_holder_name = models.CharField(max_length=200)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    card_type = models.ForeignKey('CardType', on_delete=models.CASCADE)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    current_month_usage = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.number} Expiry: {self.expiry_month}/{self.expiry_year} - {self.card_holder_name} (₹{self.current_month_usage}) | {self.card_type}'


class Deposit(models.Model):
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    time_of_deposit = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f'{self.time_of_deposit} | {self.amount} - {self.account.number}'


class Withdraw(models.Model):
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    time_of_withdraw = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f'{self.time_of_withdraw} | {self.amount} - {self.account.number}'


class Transaction(models.Model):
    sender_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name="Sender")
    receiver_account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name="Receiver")
    amount = models.FloatField()
    description = models.TextField()
    time_of_transaction = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f'{self.sender_account.number} sent {self.amount} to {self.receiver_account.number}'
    

class FixedDepositPlan(models.Model):
    name = models.CharField(max_length=200)
    miminum_amount = models.FloatField()
    mimimum_term_in_year = models.FloatField()
    maximum_term_in_year = models.FloatField()
    intrest_per_anum = models.FloatField()
    description = models.TextField()
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.name
    
class FixedDeposit(models.Model):
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    plan = models.ForeignKey('FixedDepositPlan', on_delete=models.CASCADE)
    amount = models.FloatField()
    time_of_initiation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f'{self.account.number} - INR. {self.amount} | {self.plan.name}'

    
