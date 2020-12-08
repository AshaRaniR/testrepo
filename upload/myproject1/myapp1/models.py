from django.db import models


# Create your models here.
class Hero(models.Model):
    objects = None
    name = models.TextField(max_length=60)
    alias = models.TextField(max_length=60)

def __str__(self):
        return self.name

class Diamond(models.Model):
        objects = None
        color = models.TextField(max_length=60)
        cut = models.TextField(max_length=60)
        clarity = models.TextField(max_length=60)
        caratWeight = models.TextField(max_length=60)


def __str__(self):
    return self.color

def __str__(self):
    return self.cut

def __str__(self):
    return self.clarity

def __str__(self):
    return self.caratWeight