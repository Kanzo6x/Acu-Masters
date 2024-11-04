from django.db import models

class session(models.Model):
    name = models.CharField(max_length= 250 , null= False , blank= False)
    image = models.ImageField(null= False , blank= False)
    link = models.URLField(max_length= 250 , null= False , blank= False)
