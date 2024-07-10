from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from books.models import Book
from category.models import Category
  
        
class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            category = get_object_or_404(Category, slug=cat_slug)
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['total_books'] = self.get_queryset().count()
        return context
    
    