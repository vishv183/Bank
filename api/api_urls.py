from django.urls import path
from django.views import View
from .apiviews import *
from .models import *
from .serializers import *

urlpatterns = [
    path('account/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
    path('account/', AccountList.as_view(), name = 'account-list'),
    path('Card/<int:pk>/', CardDetail.as_view(), name='card-detail'),
    path('Card/', CardList.as_view(), name = 'Card-list'),
    path('Deposit/<int:pk>/', DepositDetaiL.as_view(), name='deposit-detail'),
    path('deposit/', DepositList.as_view(), name = 'deposit-list'),
    path('withdraw/<int:pk>/', WithdrawDetail.as_view(), name='withdraw-detail'),
    path('withdraw/', WithdrawList.as_view(), name = 'withdraw-list'),
    path('transaction/<int:pk>/', TransaactionDetail.as_view(), name='transaction-detail'),
    path('transaction/', TransactionList.as_view(), name = 'transaction-list'),
    path('FixedDeposit/<int:pk>/', FixedDepositDetail.as_view(), name='FixedDeposit-detail'),
    path('FixedDeposit/', FixedDepositList.as_view(), name = 'FixedDeposit-list')
]