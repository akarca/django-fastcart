django-fastcart
===============

Django shopping cart application


INSTALLATION
------------

Install Package
***************

  ``$ pip install -e 'git+git://github.com/serdarakarca/django-fastcart.git#egg=django-fastcart'``

Settings
********
Add to INSTALLED_APPS:
  ``'fastcart',``
Add to MIDDLEWARE_CLASSES:
  ``'fastcart.middleware.CartMiddleware',``
Add to TEMPLATE_CONTEXT_PROCESSORS:
  ``'fastcart.context_processors.cart',``

Finally add this line to settings and change your model to carry with fastcart:
  ``FASTCART_PRODUCT_MODEL = 'product.Book'``

Add urls
********
  ``url(r'^cart/', include('fastcart.urls')),``

Migrate or syncdb
*****************

If you use south migrate:
  ``$ ./manage.py migrate fastcart``
or
  ``$ ./manage.py syncdb``

Usage:
**********************

Add a product to cart:
.. code:: django
  <form action="{% url 'fastcart_cart_item_list' %}" method="post">{% csrf_token %}
    <input type="hidden" name="product" value="{{ book.pk }}">
    <input type="submit" value="Add to cart">
  </form>

Remove a product from cart:
.. code:: html
  <form action="{% url 'fastcart_cart_item_delete' object.pk %}" method="post">
    {% csrf_token %}
    <input type="submit" value="Delete">
  </form>

Update quantity:
.. code:: html
  ``<form action="{% url 'fastcart_cart_item_update' object.pk %}" method="post">
    {% csrf_token %}
    <input type="text" name="quantity" value="{{ object.quantity }}">
    <input type="submit" value="Update">
  </form>``