from django import forms
from django.forms.fields import CharField

class CheckoutForm(forms.Form):
    name = CharField(required=False)
    username = CharField(required=False)
    mail = CharField(max_length=5)
    adress1 = CharField(required=False)
    adress2 = CharField(max_length=5)
    country = CharField(required=False)
    zip = CharField(max_length=5)
    payment_method = CharField(max_length=5)
    
    
class PaymentForm(forms.Form):
    name_on_card = CharField(max_length=5)  
    credit_card_no = CharField(max_length=5)
    expiration = CharField(max_length=5)
    cvv = CharField(max_length=5)
