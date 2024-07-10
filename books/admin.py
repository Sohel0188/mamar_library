from django.contrib import admin
from .models import Book, Review, BorrowedBooks

class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'is_returned', 'purchase_date')
    
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BorrowedBooks, BorrowedBooksAdmin)

