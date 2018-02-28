# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
  
class services(models.Model):
  service_name = models.CharField(max_length = 30)
  service_description = models.CharField(max_length = 100)    # in-site complains will be sent to this email too.
  service_logo_ionicon_name = models.CharField(max_length = 200)    # service_logo_ionicon_name

