from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-fastcart',
    version='1.0',
    url='http://www.github.com/serdarakarca/django-fastcart',
    download_url='https://codeload.github.com/serdarakarca/django-fastcart/zip/master',
    packages=find_packages(),
    include_package_data=True,
    license='GNU',
    author='Serdar Akarca',
    author_email='serdar@yuix.org',
    description='Django shopping cart application',
    long_description=open('README.rst').read(),
)
