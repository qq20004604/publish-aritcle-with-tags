#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render
from config.path import source_root_path


# Create your views here.
def index(request):
    return render(request, 'login.html', {
        'path': source_root_path
    })
