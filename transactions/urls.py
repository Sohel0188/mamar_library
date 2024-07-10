
from django.urls import path 
from .views import DepositMoneyView, Transaction_report

urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", Transaction_report, name="transaction_report"),

]