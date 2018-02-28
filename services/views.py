# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
 
# Create your views here.
 
from services.models import services
 
def home(request):
  #service_entries = services.objects.all() 
  content = {
    }
  return render_to_response('services.html', content)


 

