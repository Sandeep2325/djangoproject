from django.db import models
class otp(models.Model):
    email=models.EmailField(max_length=264)
    
