
from django.db import models

# Create your models here.

 
# this code creates the table named 'para_info' WHEN the migration is applied    
class landing(models.Model):
    company_name = models.CharField(max_length = 100)
    company_description = models.CharField(max_length = 500)    
    
    about_us_description1 = models.CharField(max_length = 500)
    about_us_description2 = models.CharField(max_length = 500)
    
    goal_title = models.CharField(max_length = 500)
    goal_description = models.CharField(max_length = 1000)
    
    landing_background1 = models.CharField(max_length = 100)
    landing_background2 = models.CharField(max_length = 100)
    landing_background3 = models.CharField(max_length = 100)
    
    
