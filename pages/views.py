# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')