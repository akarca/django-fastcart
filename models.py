from decimal import Decimal

from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.datastructures import SortedDict
from django.core.cache import cache
from django.contrib.auth import get_user_model

from .cart_modifiers.loader import get_cart_modifiers, get_cart_item_modifiers
from . import get_product_model

User = get_user_model()


class CartManager(models.Manager):

    def get_for_request(self, request):
        user_cart = None
        session_cart = None
        session_cart_id = None

        if 'cart' in request.session:
            session_cart_id = request.session['cart']

        if request.user.is_authenticated():
            user_cart, created = self.get_or_create(user=request.user)
            if session_cart_id:
                if session_cart_id == user_cart.pk:
                    return user_cart
                else:
                    try:
                        session_cart = self.get(pk=session_cart_id)
                        if session_cart.get_count() > 0:
                            user_cart.clear()
                            for item in session_cart.get_items():
                                item.cart = user_cart
                                item.save()
                            session_cart.clear()
                            session_cart.delete()
                            user_cart.reset_cached_items()
                    except self.model.DoesNotExist:
                        pass
            request.session['cart'] = user_cart.pk
            return user_cart

        if session_cart_id:
            try:
                session_cart = self.get(pk=session_cart_id)
                return session_cart
            except self.model.DoesNotExist:
                pass
        session_cart = self.create(user=None)
        request.session['cart'] = session_cart.pk
        return session_cart


class Cart(models.Model):
    user = models.OneToOneField(User,
                                null=True,
                                blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __init__(self, *args, **kwargs):
        super(Cart, self).__init__(*args, **kwargs)
        self.modifiers = SortedDict()
        self.set_cached_items()

    def cachekey(self):
        if self.pk:
            return 'fastcart_items_%s' % (self.pk)

    def set_cached_items(self):
        if self.cachekey():
            items = cache.get(self.cachekey())
            if items:
                self.cached_items = items
                cache.set(self.cachekey(), items, 60 * 60 * 24)
                return None
        self.reset_cached_items()

    def reset_cached_items(self):
        print 'reset cached ITEMSSSSSSSSSS'
        self.cached_items = self.items.all()
        if self.cachekey():
            try:
                cache.set(self.cachekey(), self.cached_items, 60 * 60 * 24)
            except Exception as e:
                pass

    def get_items(self):
        return self.cached_items

    def get_price(self):
        price = Decimal('0.00')
        for item in self.get_items():
            price += item.get_total_price()
        return price

    def get_count(self):
        c = 0
        for item in self.get_items():
            c = c + item.quantity
        return c

    def get_total_price(self):
        total_price = self.get_price()
        for modifier in get_cart_modifiers():
            total_price = modifier(self, total_price)
        return total_price

    def add(self, product, quantity=1):
        item, created = self.items.get_or_create(
            product=product,
            defaults={'quantity': quantity},
        )
        if not created:
            item.quantity += quantity
            item.save()
        self.reset_cached_items()
        return item

    def clear(self):
        self.items.all().delete()
        self.modifiers.clear()
        self.reset_cached_items()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items')

    product = models.ForeignKey(settings.FASTCART_PRODUCT_MODEL)
    quantity = models.PositiveIntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ('cart', 'product')

    def __init__(self, *args, **kwargs):
        super(CartItem, self).__init__(*args, **kwargs)
        self.modifiers = SortedDict()

    @property
    def unit_price(self):
        return self.product.get_price()

    def get_price(self):
        return self.unit_price * self.quantity

    def get_total_price(self):
        self.modifiers.clear()
        total_price = self.get_price()
        for modifier in get_cart_item_modifiers():
            total_price = modifier(self, total_price)
        return total_price
