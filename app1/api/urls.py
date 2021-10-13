from django.urls import path
from app1.api import views

app_name = 'app1_api'

urlpatterns = [
    path('mockupdata/<slug:slug>/', views.mocksingleproductfun, name = "mocksingleproduct"),
    path('mockupdata/', views.MockupViewView.as_view(), name = "mockupdata"),
]   