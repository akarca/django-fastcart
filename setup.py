from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-fastcart',
    version='0.1dev',
    url='http://www.github.com/serdarakarca/django-fastcart',
    packages=find_packages(),
    include_package_data=True,
    license='GNU',
    author='Serdar Akarca',
    author_email='serdar@yuix.org',
    description='Django shopping cart application',
    long_description=open('README.rst').read(),
)
