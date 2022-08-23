from urllib import request
from django import forms
from api.models import Account
from users.models import User


class WithdrawForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(WithdrawForm, self).__init__(*args, **kwargs)

        self.fields['account'] = forms.ModelChoiceField(
            queryset=Account.objects.filter(user=User.objects.get(id=user.id)),
            empty_label='Select Account',
            widget=forms.Select(

                attrs={
                    'class': 'form-control'
                }
            )
        )

    amount = forms.FloatField(
        widget=forms.NumberInput(
            attrs= {
                'class': 'form-control form-input'    
            }
        )
    )
    
    description = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                'placeholder': 'Description (Optional)',
                'class': 'form-control form-control-lg'
            }
        )
    )
