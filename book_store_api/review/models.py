from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=25)
    birthdate=models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Comment(models.Model):
    body=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

class Review(models.Model):
    title=models.CharField(max_length=30)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title