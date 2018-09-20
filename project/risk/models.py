from django.contrib.postgres.fields import JSONField
from django.db import models

class Risk(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name
        
class Field(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('date', 'Date'),
        ('number', 'Number'),
    )    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='text')
    label = models.CharField(max_length=100)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name