from django.db import models

class Admin(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'
    
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()  
    password = models.CharField(max_length=128)  
    phone = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1,choices=Gender.choices,default=Gender.OTHER,)
    address = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


