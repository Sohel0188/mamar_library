from django.contrib import admin
from django.urls import path, include 
from .views import HomeView

# media file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', HomeView.as_view(), name='category_wise_book'),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('books/', include('books.urls')),
    # path('books/', include('books.urls')),
    # path('transactions/', include('transactions.urls')),
    # path('category/', include('category.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)