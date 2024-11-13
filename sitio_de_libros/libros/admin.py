from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
   
    list_display = ('titulo', 'valoracion', 'fecha_creacion', 'fecha_modificacion')

    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

    list_filter = ('valoracion', 'fecha_modificacion')

    admin.site.register(Book, BookAdmin)
