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