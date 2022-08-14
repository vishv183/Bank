from cgitb import lookup
from dataclasses import fields
import imp
from rest_framework import serializers
from .models import *

    
class AccountSerializer(serializers.ModelSerializer):
    class meta: 
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
            'account_type'
        ]
    extra_kwargs = {}
