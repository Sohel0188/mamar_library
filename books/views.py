from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from books.models import Book,BorrowedBooks
from transactions.models import Transaction
from django.contrib import messages
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.core.mail import send_mail
from django.conf import settings
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
        
        
def buy_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user.account
    if not BorrowedBooks.objects.filter(book=book, user=request.user.account).exists():
        if user.balance >= book.price:
            BorrowedBooks.objects.create(book=book, user=request.user.account)
            book.qunatity -= 1 
            book.save()
            user.balance -= book.price
            user.save()
            Transaction.objects.create(user=request.user.account, amount=book.price, transaction_type='buy_book')
            messages.success(request, 'You have successfully borrowed the book.')
            send_transaction_email( request.user, book.price, "Message", "books/message.html")
        else:
            messages.error(request, 'Insufficient balance to borrow the book.Please deposit money.')
    else:
            messages.error(request, 'Already Purchased')     
            
   
    return redirect('profile')


def return_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBooks, pk=borrowed_book_id)
    borrowed_book.is_returned = True
    borrowed_book.save()
    user = borrowed_book.user
    user.balance += borrowed_book.book.price
    user.save()
    messages.success(request, 'You have successfully returned the book. The book price is added with your main balance. ')
    return redirect('profile')


class DetailPostView(DetailView):
    model = Book
    pk_url_kwarg = 'id'
    template_name = 'books/details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.ReviewForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object 
        comments = book.comments.all()
        review_permission = False
        if  BorrowedBooks.objects.filter(book=book, user=self.request.user.account).exists():
            review_permission = True
            comment_form = forms.ReviewForm()
        else:
            comment_form = ""
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['review_permission'] = review_permission 
        return context
    
    
    
    