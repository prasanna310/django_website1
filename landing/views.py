# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
 
# Create your views here.
 
from models import landing
 
def home(request):

  content = {

    }
  return render_to_response('landing.html', content)


 

