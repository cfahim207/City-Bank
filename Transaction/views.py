from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Transaction.models import Transaction
from .forms import DepositForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

from django.shortcuts import redirect
# Create your views here.

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()   
    
    

class DepositMoneyView(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    form_class = DepositForm
    success_url = reverse_lazy('profile')
    

    def form_valid(self, form):
        
        amount = form.cleaned_data.get('amount')
        
        account = self.request.user.account
        account.balance += amount # amount = 200, tar ager balance = 0 taka new balance = 0+200 = 200
        account.save(
            update_fields=[
                'balance'
            ]
        )
        transaction = form.save(commit=False)
        transaction.account=account
        transaction.balance_after_transaction=account.balance
        transaction.save()
        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "deposite_email.html")
        
        
        return super().form_valid(form)
    
