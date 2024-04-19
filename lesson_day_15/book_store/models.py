from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=100)
    published_date=models.DateTimeField()
    isbn=models.CharField(max_length=14)
    pages=models.IntegerField()
    summary=models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"
    
# Newspaper гэдэг  model үүсгээд дор хаяж 5 ширхэг  
    
class Newspaper(models.Model):
    title=models.CharField(max_length=255)
    published_date=models.DateTimeField()
    summary=models.TextField()
    company=models.CharField(max_length=35)
    pages=models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.published_date}"