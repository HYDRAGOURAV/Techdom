from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index , name="index"),
    path('Register', views.Register , name="Register"),
    path('Login', views.Login , name="Login"),
    path('add_loan_details', views.add_loan_details , name="add_loan_details"),
    path('show', views.show , name="show"),
    path('add_REpayment', views.add_REpayment , name="add_REpayment"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)