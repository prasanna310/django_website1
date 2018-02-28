# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class company_name(models.Model):
  company_name = models.CharField(max_length = 50)
  company_logo_img = models.CharField(max_length = 200)    


class contact(models.Model):
  contact_address = models.CharField(max_length = 100)
  contact_email = models.CharField(max_length = 100)    # in-site complains will be sent to this email too.
  contact_phone = models.CharField(max_length = 100)  

  address_x= models.CharField(max_length = 20)  
  address_y= models.CharField(max_length = 20)      

  company_facebook = models.CharField(max_length = 100) 
  company_linkedin = models.CharField(max_length = 100) 
  company_twitter = models.CharField(max_length = 100) 
  company_instagram = models.CharField(max_length = 100) 
  
