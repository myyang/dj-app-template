#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup, find_packages

from distutils.core import Command


class TestCommand(Command):

    """App test command"""
    user_options = []

    def run(self):
        """Run test """
        from django.conf import settings
        settings.configure(
            DATABASES={'default': {'NAME': ':memory:', 'ENGINE': 'django.db.backends.sqlite3'}},
            INSTALLED_APPS=settings.INSTALLED_APPS + ['{{cookiecutter.app_name}}']
        )

        from django.core.management import call_command
        import django

        django.setup()
        call_command('test', '{{cookiecutter.app_name}}')


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='{{cookiecutter.app_name}}',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    long_description=README,
    url='',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
