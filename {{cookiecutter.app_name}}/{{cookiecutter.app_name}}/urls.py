#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    "",
    url("^$", 'viewfunc', name='root-of-app'),
)
