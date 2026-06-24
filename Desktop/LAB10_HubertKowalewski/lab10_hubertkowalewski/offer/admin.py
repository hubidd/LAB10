from django.contrib import admin
from .models import Kategoria, Szkolenie, Rejestracja

@admin.register(Szkolenie)
class SzkolenieAdmin(admin.ModelAdmin):
    list_display = ('numer', 'kategoria', 'cena', 'liczba_godzin', 'publikuj')
    list_filter = ('kategoria', 'publikuj') 
    search_fields = ('numer',)              
    ordering = ('kolejnosc',)               

admin.site.register(Kategoria)
admin.site.register(Rejestracja)