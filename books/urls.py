
from django.urls import path 
from . import views

urlpatterns = [
    path("buy_book/<int:book_id>", views.buy_book, name="buy_book"),
    path("return_book/<int:borrowed_book_id>", views.return_book, name="return_book"),
     path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),

]