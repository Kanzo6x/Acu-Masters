from django.db import models

class iti_course(models.Model):
    name = models.CharField(max_length= 250 , null= False , blank= False)
    link = models.URLField(max_length= 250 , null= False , blank= False)
