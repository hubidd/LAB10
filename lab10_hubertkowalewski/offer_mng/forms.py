from django import forms
from offer.models import Kategoria, Szkolenie 

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'tytul', 'opis', 'kategoria_nadrzedna', 'publikuj', 'kolejnosc']

class SzkolenieForm(forms.ModelForm):
    class Meta:
        model = Szkolenie
        fields = ['numer', 'cena', 'liczba_godzin', 'kategoria', 'publikuj', 'kolejnosc']