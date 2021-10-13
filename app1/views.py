from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,CartItem,Order
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CheckoutForm, PaymentForm
from django.contrib.auth.models import User
import requests
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist


class IndexView(ListView):
    model = Item
    paginate_by = 10
    template_name = "homepage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items_list'] = Item.objects.all()
        return context


def checkoutfun(request):
    order = Order.objects.get(user=request.user, ordered=False)
    form = CheckoutForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        adress1 = form.cleaned_data.get("adress1")
        adress2 = form.cleaned_data.get("adress2")
        country = form.cleaned_data.get("country")
        zip = form.cleaned_data.get("zip")
        payment_method = form.cleaned_data.get("payment_method")
  
        context = {
         "name" : User.username ,
         "username " : User.username ,
         "email" : email ,
         "adress1" : adress1, 
         "adress2" : adress2 ,
         "country" : country ,
         "zip" : zip,
         }

        return redirect("app1:payment")
    return render(request,"checkout.html", {'object': order, "form": form})

def addtocartfun(request, slug):
    item = get_object_or_404(Item, slug=slug)
    try:
        cart = CartItem.objects.get(item=item,user = request.user)
    except:
        cart = CartItem.objects.create(item=item,user = request.user)
    toSummary = Order.objects.filter(user=request.user, ordered=False)
    if toSummary.exists():
        tooSummary = toSummary[0]
        if not tooSummary.items.filter(item__slug=item.slug).exists():
            tooSummary.items.add(cart)   
            return redirect("app1:ordersummary")
        else:
            print('*********toSummary')
            tooSummary = toSummary[0]
            cart.quantity += 1
            cart.save()
            return redirect("app1:ordersummary")
    else:
        toSummary = Order.objects.create(user=request.user, ordered=False)
        toSummary.items.add(cart)   
        return redirect("app1:ordersummary")





def removefromcartfun(request,slug):
    item = get_object_or_404(Item, slug=slug)
    toSummary = Order.objects.filter(user=request.user, ordered=False)
    if toSummary.exists():
        tooSummary = toSummary[0]
        # check if the order item is in the order
        if tooSummary.items.filter(item__slug=item.slug).exists():
            order_item = CartItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            tooSummary.items.remove(order_item)
            order_item.delete()
            messages.info(request, "Item is removed")
            return redirect("app1:singleproduct", slug = slug)
        else:
            messages.info(request, "It was not in your cart")
            return redirect("app1:singleproduct", slug = slug)

    else:
        messages(request,"Order does not exists")
        return redirect("app1:singleproduct", slug = slug)

    
def ordersummaryfun(request):
    order = Order.objects.get(user=request.user, ordered=False)
    context = {
            'object': order
        }
    return render(request, 'ordersummary.html', context)


def paymentfun(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        name_on_card = form.cleaned_data.get("name_on_card")
        credit_card_no = form.cleaned_data.get("credit_card_no")
        expiration = form.cleaned_data.get("expiration")
        cvv = form.cleaned_data.get("cvv")
        context = {
            "name_on_card" : name_on_card,
            "credit_card_no" : credit_card_no,
            "expiration" : expiration,
            "cvv" : cvv
        }
        messages.info(request, "Payment Successfull")
        return redirect("app1:home")
    return render(request,"payment.html", {"form" : form})



def singleproductfun(request,slug):
    item = get_object_or_404(Item, slug=slug)
    context = {
        "item" : item
    }
    return render(request,"singleproduct.html",context)
