from django.contrib import admin

from .models import Book, BiblicalVerse

class VerseAdmin(admin.ModelAdmin):
    search_fields = ['verse_title']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Book, BookAdmin)
admin.site.register(BiblicalVerse, VerseAdmin)

