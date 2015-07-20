from django.contrib import admin

from .models import BookReader
from .models import Book
from .models import Author
from .models import Country


admin.site.register(BookReader)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Country)
