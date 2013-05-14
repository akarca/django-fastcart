from django.conf.urls.defaults import patterns, url
from .views import CartItemListView, CartItemUpdateView, CartItemDeleteView


urlpatterns = patterns('',
                       url(r'^$',
                           CartItemListView.as_view(),
                           name='fastcart_cart_item_list'),

                       url(r'^update/(?P<pk>\d+)/?$',
                           CartItemUpdateView.as_view(),
                           name='fastcart_cart_item_update'),

                       url(r'^delete/(?P<pk>\d+)/?$',
                           CartItemDeleteView.as_view(),
                           name='fastcart_cart_item_delete'),

                       )
