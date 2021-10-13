from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.IndexView.as_view(),name = "home"),
    path('product/<slug:slug>', views.singleproductfun, name = "singleproduct"),
    path('checkout/', views.checkoutfun, name = "checkout"),
    path('ordersummary/', views.ordersummaryfun, name = "ordersummary"),
    path('addtocart/<slug:slug>', views.addtocartfun, name = "addtocart"),
    path('removefromcart/<slug:slug>', views.removefromcartfun, name = "removefromcart"),
    path('payment/', views.paymentfun, name='payment'),
]   



