from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy


from .forms import CartItemForm, UpdateCartItemForm
from .models import Cart


class CartItemListView(ListView):

    def get_queryset(self):
        return self.request.cart.items.all()

    def post(self, request, *args, **kwargs):
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.add_to_cart(request.cart)
            if request.is_ajax():
                return HttpResponse(
                    json.dumps({
                               'result': 'success',
                               'count': request.cart.get_count(),
                               'total': request.cart.get_total_price(),
                               }),
                    mimetype="application/json")
        elif request.is_ajax():
            return HttpResponse(
                json.dumps({
                    'result': 'fail',
                    'count': request.cart.get_count(),
                    'total': request.cart.get_total_price(),
                }),
                mimetype="application/json")
        return redirect('fastcart_cart_item_list')


class CartItemDeleteView(DeleteView):
    success_url = reverse_lazy('fastcart_cart_item_list')

    def get_queryset(self):
        return self.request.cart.items.all()


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
                    json.dumps({
                        'result': 'success',
                        'count': request.cart.get_count(),
                        'total': request.cart.get_total_price(),
                    }),
                    mimetype="application/json")
        return redirect(self.success_url)
