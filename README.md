django-fastcart
===============

Django shopping cart application

Installation:
-------------

## Install Package

pip install -e 'git+git://github.com/serdarakarca/django-fastcart.git#egg=django-fastcart'

## Add to INSTALLED_APPS

INSTALLED_APPS = (
  ...
  'fastcart',
  ...
)

## Settings

FASTCART_PRODUCT_MODEL = 'product.Book'

## Add urls

url(r'^cart/', include('fastcart.urls')),

## Migrate or syncdb

If you use south migrate: ./manage.py migrate fastcart
or
./manage.py syncdb