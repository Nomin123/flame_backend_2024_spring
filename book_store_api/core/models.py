from django.db import models

# Create your models here.
class Contributor(models.Model):
    first_names=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.EmailField()

class Publisher(models.Model):
    name=models.CharField(max_length=50, default="Az Hur")
    website=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=70, help_text="Title of the book" , default="Test") 
    publication_date=models.DateField(verbose_name="Date the book is published",auto_now_add=True, blank=True)
    isbn=models.CharField(max_length=20)
    publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.publisher}"
    
