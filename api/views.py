from django.http import HttpResponse
from .models import *
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from datetime import datetime
from .serializers import *
from users.models import User

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepositDetaiL(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]    

class WithdrawDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]


class WithdrawList(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]  
    
class TransaactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class FixedDepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FixedDeposit.objects.all()
    serializer_class = FixedDepositSerializer
    permission_classes = [permissions.IsAuthenticated]


class FixedDepositList(generics.ListCreateAPIView):
    queryset = FixedDeposit.objects.all()
    serializer_class = FixedDepositSerializer
    permission_classes = [permissions.IsAuthenticated] 
    


@api_view(['GET', ])
def get_user_details(request):
    user = User.objects.get(id=int(request.user.id))
    data = {}
    data['username'] = user.user_name
    data['first_name'] = user.first_name
    data['last_name'] = user.last_name
    data['email'] = user.email
    return Response(data)
    