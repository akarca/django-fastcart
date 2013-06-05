from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from shop.models import WishCart
from custom_sites.localstorage import get_site

from .forms import CartItemForm, UpdateCartItemForm
from .models import Cart
from .utils import dumps


class CartItemListView(ListView):

    def get_queryset(self):
        return self.request.cart.items.all()

    def get_context_data(self, **kwargs):
        context = super(CartItemListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            wishcart, created = WishCart.objects.get_or_create(user=self.request.user, site=get_site())
            context['wishcart'] = wishcart
        return context

    def post(self, request, *args, **kwargs):
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.add_to_cart(request.cart)
            if request.is_ajax():
                return HttpResponse(
                    dumps({
                          'result': 'success',
                          'count': request.cart.get_count(),
                          'total': request.cart.get_total_price(),
                          }),
                    mimetype="application/json")
        elif request.is_ajax():
            return HttpResponse(
                dumps({
                    'result': 'fail',
                    'count': request.cart.get_count(),
                    'total': request.cart.get_total_price(),
                }),
                mimetype="application/json")
        return redirect('fastcart_cart_item_list')


class CartItemUpdateView(SingleObjectMixin, View):
    success_url = reverse_lazy('fastcart_cart_item_list')

    def get_queryset(self):
        return self.request.cart.items.all()

    def post(self, request, *args, **kwargs):
        form = UpdateCartItemForm(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse(
                    dumps({
                        'result': 'success',
                        'count': request.cart.get_count(),
                        'total': request.cart.get_total_price(),
                    }),
                    mimetype="application/json")
        return redirect(self.success_url)


class CartItemDeleteView(SingleObjectMixin, View):
    success_url = reverse_lazy('fastcart_cart_item_list')

    def get_queryset(self):
        return self.request.cart.items.all()

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        if request.is_ajax():
            return HttpResponse(dumps({
                'result': 'success',
                'count': request.cart.get_count(),
                'total': request.cart.get_total_price(),
            }),
                mimetype="application/json")
        return redirect(self.success_url)
