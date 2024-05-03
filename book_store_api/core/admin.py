from django.contrib import admin
from .models import Contributor,Book,Publisher



# Register your models here.
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(Publisher)
