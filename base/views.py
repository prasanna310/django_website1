# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
 
# Create your views here.
from models import contact, company_name

def home(request):
   
  company_name_entries = company_name.objects.all()[0] 
  content = {
    'company_name_entries':company_name_entries,
    }
  return render_to_response('base.html', content)

 

# service and work tabs are same, for now 
def base_with_work(request):
   
  content = {
    }
  return render_to_response('service.html', content)


def base_with_service(request):
   
  content = {
    }
  return render_to_response('service.html', content)





# support and contact tabs are same, for now
def base_with_support(request):
   
  contact_entries = contact.objects.all()[0] # first item   
  content = {
    'contact_entries':contact_entries,
    }
  return render_to_response('contact.html', content)


def base_with_contact(request):
  contact_entries = contact.objects.all()[0] # first item   
  content = {
    'contact_entries':contact_entries,
    }
  return render_to_response('contact.html', content)

