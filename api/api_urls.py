from django.urls import path
from django.views import View
from .apiviews import *
from .models import *
from .serializers import *

urlpatterns = [
    path('account/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
    path('account/', AccountList.as_view(), name = 'account-list')
]