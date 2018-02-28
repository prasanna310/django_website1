# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import contact, company_name

# Register your models here.
admin.site.register(contact)
admin.site.register(company_name)