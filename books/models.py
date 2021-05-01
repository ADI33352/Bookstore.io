from django.db import models

# Create your models here.
class Data(models.Model):
    heading = models.CharField(max_length=100,default = '')
    subheading = models.CharField(max_length=100,default = '')
    content = models.TextField()
    imagee = models.ImageField(upload_to ='images', default = '')
    link = models.URLField(max_length=200,default='')

    def __str__(self):
        return self.heading
    
    

class Contact(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    subject=models.CharField(max_length=50,default='')
    message=models.TextField(max_length=500,default='')

    def __str__(self):
        return self.name
    

    

   
