from django.db import models

# Create your models here.
class Dog(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    type = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000)
    cool_dog = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']