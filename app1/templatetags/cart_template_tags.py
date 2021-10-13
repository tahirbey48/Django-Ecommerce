from django import template
from app1.models import CartItem



register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        cart = CartItem.objects.filter(user=user, ordered=False)
        if cart.exists():
            return cart.count()
        else:
            return 0