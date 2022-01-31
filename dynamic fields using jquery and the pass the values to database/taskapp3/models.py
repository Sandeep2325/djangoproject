from django.db import models

class fields(models.Model):
    fullname = models.CharField(null=False,blank=True,max_length=50)
    hobbies = models.TextField(null=True,blank=True,)

