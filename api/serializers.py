from cgitb import lookup
from dataclasses import fields
import imp
from rest_framework import serializers
from .models import *

    
class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        lookup_field = 'pk'
        fields = [
            'pk',
            'number',
            'ifsc',
            'balance',
            'holder_name',
            'holder_email',
            'holder_phone',
            'holder_phone',
            'account_type'
        ]
    extra_kwargs = {}
    
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        lookup_field = 'pk'
        fields = [
            'pk',
            'number',
            'card_holder_name',
            'expiry_month',
            'expiry_year',
            'card_type',
            'account',
            'current_month_usage'
        ]
        
    extra_kwargs = {}
    
class DepositSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Deposit
        lookup_field = 'pk'
        fields = [
            'pk',
            'account',
            'description',
            'time_of_deposit'     
        ]
        
    extra_kwargs = {}

class WithdrawSerializer(serializers.Model):
    class Meta: 
        model = Withdraw
        lookup_field = 'pk'
        fields = [
            'pk',
            'account',
            'description',
            'time_of_withdraw'     
        ]
        
    extra_kwargs = {}
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        lookup_field = 'pk'
        fields = [
            'pk',
            'sender_account',
            'reciever_account',
            'amount',
            'description',
            'time_of_transaction',
            'Status'         
        ]
        
    extra_kwargs = {}
    
class FixedDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedDeposit
        lookup_field = 'pk'
        fields = [
            'pk',
            'account',
            'plan',
            'amount',
            'time_of_initiation'
        ]
        
    extra_kwargs = {}