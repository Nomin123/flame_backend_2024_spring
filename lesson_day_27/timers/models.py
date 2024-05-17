from django.db import models

# Create your models here.
class Timer(models.Model):
    title=models.CharField(max_length=50)
    project=models.CharField(max_length=50)
    elapsed=models.IntegerField(null=True)
    running_since=models.IntegerField(null = True)