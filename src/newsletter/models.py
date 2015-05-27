from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,blank=True, null=True)  #For CharField max_length is necessary
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    #First Field to Show
    def __unicode__(self): #__str__ is used for Python 3
        return self.email
