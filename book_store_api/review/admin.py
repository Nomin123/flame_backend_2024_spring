from django.contrib import admin
from .models import Review,Author, Comment


# Register your models here.
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Comment)


