from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserSignUpForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from .models import UserAccount
from books.models import BookModel
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()   
    

class SignUpView(FormView):
    template_name ='signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLogin(LoginView):
    template_name='user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
         
def UserProfile(request):     
    return render(request,"profile.html")


# class Update_profile(View):
#     template_name = 'update_profile.html'

#     def get(self, request):
#         form = UserUpdateForm(instance=request.user)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#         return render(request, self.template_name, {'form': form})  

def borrow(request,id):
    data=BookModel.objects.filter(pk=id)
    book=BookModel.objects.get(pk=id)
    account=request.user.account
    price=book.borrowing_price
    if account.balance>price:  
        account.balance-=price
    account.save()
    send_transaction_email(request.user, price, "Borrow Book Message", "borrow_book_email.html")
    return render(request,"profile.html",{'data':data})