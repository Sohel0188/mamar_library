from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout 
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from books.models import BorrowedBooks

# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) 
    
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserAccountUpdate(View):
    template_name = 'accounts/profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance= request.user)
        borrowed_books = BorrowedBooks.objects.filter(user=request.user.account)
        return render (request, self.template_name, {'form': form, 'borrowed_books': borrowed_books })
    
    def post (self, request):
        form = UserUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect ('profile')

        return render (request, self.template_name, {'form' : form})
# def home(request):
#     return render(request, 'accounts/registration.html')


