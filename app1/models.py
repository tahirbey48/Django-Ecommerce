from django.db import models
from django.conf import settings
from django.urls import reverse

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    def __str__(self):          
        return self.title

    def get_absolute_url(self):
        return reverse("app1:singleproduct", kwargs= {"slug" : self.slug})

    def get_add_to_cart_url(self):
        return reverse("app1:addtocart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("app1:removefromcart", kwargs={'slug': self.slug})


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def get_total_single_item_price(self):
        return self.quantity * self.item.price   

        
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_total_amount(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_single_item_price()
        return total


class MockupItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def get_that_url(self): #kwargs, what I want to pass to my view
        return reverse("app1_api:mocksingleproduct", kwargs= {"slug" : self.slug})

        