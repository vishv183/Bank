from django.contrib import admin
from .models import *


admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(CardType)
admin.site.register(Card)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(Transaction)
admin.site.register(FixedDepositPlan)
admin.site.register(FixedDeposit)
