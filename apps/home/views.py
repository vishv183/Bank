# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from api.models import *
from django.shortcuts import render
from .forms import *




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    account = Account.objects.get(user=request.user.id)
    context['acc_no'] = account.number
    context['balance'] = account.balance
    context['ifsc'] = account.ifsc
    context['account_type'] = account.account_type
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def home(request):
    context = {'segment': 'index'}
    account = Account.objects.get(user=request.user.id)
    context['acc_no'] = account.number
    context['balance'] = account.balance
    context['ifsc'] = account.ifsc
    context['account_type'] = account.account_type
    html_template = loader.get_template('home/index-testing.html')
    return HttpResponse(html_template.render(context, request))





@login_required(login_url='/login/')
def withdraw(request):
    context = {'segment': 'withdraw'}
    
    if request.method == 'POST':
        data = dict(request.POST)
        
        account = Account.objects.get(id=int(data['account'][0]))
        
        account.balance -= float(data['amount'][0])
        
        account.save()
        
        withdraw_transaction = Withdraw()
        withdraw_transaction.account = account
        withdraw_transaction.amount = float(data['amount'][0])
        withdraw_transaction.description = data['description'][0]
        withdraw_transaction.save()
    
    form = WithdrawForm(user = request.user)
    
    context['form'] = form
    
    return render(request, 'home/withdraw.html', context)
    
    
    
    
    

@login_required(login_url='/login/')
def deposit(request):
    context = {'segment': 'deposit'}
    
    return render(request, 'home/deposit', context)

@login_required(login_url='/login/')
def transfer(request):
    context = {'segment': 'transfer'}
    
    return render(request, 'home/transfer.html', context)
    

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        print(context)

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
