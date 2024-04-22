from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    # author=models.CharField(max_length=100)
    published_date=models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
    
class Review(models.Model):
    Comment=models.CharField(max_length=100)
    Author=models.CharField(max_length=20)
    Dates=models.DateTimeField()


    def __str__(self):
        return f"{self.Author}"