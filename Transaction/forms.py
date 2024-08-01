from django import forms
from .models import Transaction

class DepositForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=["amount"]
        
    # def clean_amount(self): # amount field ke filter korbo
    #     min_deposit_amount = 100
    #     amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
    #     if amount < min_deposit_amount:
    #         raise forms.ValidationError(
    #             f'You need to deposit at least {min_deposit_amount} $'
    #         )

    #     return amount
    
    # def save(self, commit=True):
    #     self.instance.account = self.account
    #     self.instance.balance_after_transaction = self.user_account.balance
    #     return super().save()
    # amount=forms.IntegerField()
    