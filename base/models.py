from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    simage = models.ImageField(upload_to='uploads/',default='Default.webp')

#upload_to='uploads/' - whenever the user is uploading an image, store inside the uploads folder

#default='Default.webp' - if user is not uploading any img then which file i need to store 

#image will not be store in the database only the file name will be stored 
#uploads/pic.jpg
#Default.webp

#pip install pillow