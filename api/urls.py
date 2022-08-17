from django.urls import path
from django.views import View
from .views import *
from .models import *
from .serializers import *

urlpatterns = [
    path('account/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
    path('accounts/', AccountList.as_view(), name = 'accounts-list'),
    path('card/<int:pk>/', CardDetail.as_view(), name='card-detail'),
    path('cards/', CardList.as_view(), name = 'Card-list'),
    path('deposit/<int:pk>/', DepositDetaiL.as_view(), name='deposit-detail'),
    path('deposits/', DepositList.as_view(), name = 'deposit-list'),
    path('withdraw/<int:pk>/', WithdrawDetail.as_view(), name='withdraw-detail'),
    path('withdrawals/', WithdrawList.as_view(), name = 'withdraw-list'),
    path('transaction/<int:pk>/', TransaactionDetail.as_view(), name='transaction-detail'),
    path('transactions/', TransactionList.as_view(), name = 'transaction-list'),
    path('fd/<int:pk>/', FixedDepositDetail.as_view(), name='FixedDeposit-detail'),
    path('fds/', FixedDepositList.as_view(), name = 'FixedDeposit-list'),
    path('getuser/', get_user_details, name='get-users')
]