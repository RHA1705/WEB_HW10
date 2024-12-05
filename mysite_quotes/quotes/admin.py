from django.contrib import admin
from .models import Quotes, Tag, Author

admin.site.register(Quotes)
admin.site.register(Tag)
admin.site.register(Author)
