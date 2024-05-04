from django.db import models

from django.contrib.auth.models import User

class Loan_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    User_email = models.EmailField(max_length=23)
    User_number = models.BigIntegerField()
    amount_required = models.DecimalField(max_digits=10, decimal_places=2)
    currant_Date = models.DateTimeField(auto_now_add=True) 
    loan_term = models.IntegerField() 
    approved = models.BooleanField(default=False)

class LoanRepayment(models.Model):
    loan = models.ForeignKey(Loan_details, on_delete=models.CASCADE,null=True)
    repayment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_date = models.DateField()