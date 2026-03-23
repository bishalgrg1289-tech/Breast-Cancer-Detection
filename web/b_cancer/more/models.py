from django.db import models

# Create your models here.

class info(models.Model):
    Tumer=models.CharField(max_length=15)
    image=models.ImageField(upload_to='b_type/')

    
    def __str__(self):
        return self.name
