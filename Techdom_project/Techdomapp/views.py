from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import datetime
from . models import Loan_details,LoanRepayment
def index(req):
    return render(req,"index.html")
def Register(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        email = req.POST.get("email")
        user = User.objects.create_user(username=username,password=password)
        user.email = email
        user.save()
        return HttpResponse("User saved")
    else:
        return render(req,"register.html")
def Login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(req,user)
            return render(req,"Main_Page.html")
        else:
            return HttpResponse("No User found")
    else:
        return render(req,"login.html")

def add_loan_details(req):
    if req.method == "POST":
        User_email = req.POST.get('User_email')
        User_number = req.POST.get('User_number')
        amount_required = req.POST.get('amount_required')
        loan_term  = req.POST.get('loan_term')
        User_loan = Loan_details(User_email = User_email, User_number = User_number,amount_required= amount_required,loan_term= loan_term)
        User_loan.save()
        amount = amount_required/loan_term
        amount_ = amount
        # for i in range(loan_term):
        #     amount_paid = amount
        #     amount_remaining = amount_required - amount_paid
        loan_details_dict = Loan_details.objects.all()
        User_Data = {
            'loan_details_dict':loan_details_dict,
        }
        return render(req,'User_Loan_details.html',User_Data,{'amount_':amount_})
    else:
        return render(req,"add_loan_details.html")
    
def show(req):
    loan_details_dict = Loan_details.objects.get()
    amount = loan_details_dict.amount_required
    loan_term = loan_details_dict.loan_term
    amount_ = amount/loan_term
    The_Data = LoanRepayment.objects.get()
    User_Data = {
            'loan_details_dict':loan_details_dict,
            'amount_':amount_,
            'The_Data':The_Data,
    }
    return render(req,"User_Loan_details.html",User_Data,)

def approve_loan(request, loan_id):
    loan = get_object_or_404(Loan_details, pk=loan_id)
    loan.approved = True
    loan.save()
    return render(request, 'loan_approved.html', {'loan': loan})

def add_REpayment(req):
    if req.method =="POST":
        repayment_amount = req.POST.get('repayment_amount')
        repayment_date = req.POST.get('repayment_date')
        The_re = LoanRepayment(repayment_date=repayment_date, repayment_amount= repayment_amount)
        The_re.save()
        The_Data = LoanRepayment.objects.get()
        context = {
            'The_Data':The_Data,
        }
        return render(req,'User_Loan_details.html',context)

    