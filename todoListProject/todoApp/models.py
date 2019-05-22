from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class todoModel(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title