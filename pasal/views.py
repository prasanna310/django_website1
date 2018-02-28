# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
 
# Create your views here.
 
from landing.models import landing
from services.models import services
from base.models import contact, company_name

#from landing import views  as landing_views
 
def home(request):  
  company_name_entries = company_name.objects.all()[0] 
  landing_entries = landing.objects.all()[0] # first item?  #objects.filter(headline='test')
  service_entries = services.objects.all() # first item?  #objects.filter(headline='test')
  #contact_entries = contact.objects.all()[0] # first item? 
  
  
  content = {
    'landing_entries':landing_entries,
    'service_entries':service_entries,
    'company_name_entries':company_name_entries,
    #'contact_entries':contact_entries,

    }
  return render_to_response('index.html', content)



