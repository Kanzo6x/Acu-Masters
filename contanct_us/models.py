from django.db import models
class members(models.Model):
    image = models.ImageField(default= '../static/imags/default_image.png' , null= False)
    name = models.CharField(max_length= 250 , null= False , blank= False)
    description = models.CharField(max_length= 1000 , null= False , blank= False)
    is_heading = models.BooleanField(null= False , blank= False)
    team_code = models.IntegerField(null= False , blank= False)
    facebook_link = models.CharField(max_length=1000 , null= False , blank= False)
    linkedin_link = models.CharField(max_length=1000 , null= False , blank= False)
    
    
