from pickle import TRUE
from django.db import models

class Info(models.Model):
    firstname=models.CharField(max_length=50,null=True,blank=True)
    lastname=models.CharField(max_length=50,null=True,blank=True)
    dob=models.DateField(null=True)


    #Relationship=models.CharField(max_length=20)


    #gender=models.CharField(max_length=10)

    CHOICES = (('S','single'),('M','married'))
    Relationship=models.CharField(max_length=20, choices=CHOICES,null=True)

    CHOICES1 = (('M','male'),('F','female'))
    gender=models.CharField(max_length=20, choices=CHOICES1,null=True)

    lang=models.CharField(max_length=50,null=True, blank=True)
    hobbies=models.TextField(null=True)
    picture=models.ImageField(upload_to="records",null=True)
    email=models.EmailField(null=True)
    phone=models.BigIntegerField(null=True)
    door=models.IntegerField(null=True)
    street=models.TextField(null=True)
    city=models.CharField(max_length=50,null=True)
    dist=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50,null=True)
    code=models.IntegerField(null=True)
    course=models.CharField(max_length=150,null=True)
    institute=models.CharField(max_length=150,null=True)
    address=models.TextField(null=True)
    started=models.DateField(null=True)
    passed=models.DateField(null=True)
    #gpa=models.DecimalField(decimal_places=2,max_digits=5)
    gpa=models.IntegerField(null=True)
    resume=models.FileField(upload_to="records",null=True)
    password=models.CharField(max_length=20,null=True)
    confirm_password=models.CharField(max_length=20,null=True)
