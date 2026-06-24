from django.shortcuts import render, get_object_or_404
from .models import Kategoria, Szkolenie
from django.http import JsonResponse
from django.core import serializers
from .models import Rejestracja
from django import forms

def kategorie_list(request):
    kategorie = Kategoria.objects.filter(publikuj=True).order_by('kolejnosc')
    return render(request, 'offer/kategorie.html', {'kategorie': kategorie})

def szkolenia_list(request, kategoria_id):
    kategoria = get_object_or_404(Kategoria, id=kategoria_id)
    szkolenia = Szkolenie.objects.filter(kategoria=kategoria, publikuj=True).order_by('kolejnosc')
    return render(request, 'offer/szkolenia.html', {'kategoria': kategoria, 'szkolenia': szkolenia})

def api_categories(request):
    kategorie_stale = [
        {"id": 1, "nazwa": "Zarządzanie oświatą"},
        {"id": 2, "nazwa": "Edukacja informatyczna"},
        {"id": 3, "nazwa": "Psychoedukacja"}
    ]
    return JsonResponse(kategorie_stale, safe=False)

def api_courses(request):
    szkolenia = list(Szkolenie.objects.values('id', 'numer', 'cena', 'liczba_godzin'))
    return JsonResponse(szkolenia, safe=False)

def wyszukiwarka_szkolen(request):
    wyniki = Szkolenie.objects.all()
    
    wyniki = wyniki.filter(publikuj=True)
    
    zapytanie = request.GET.get('q')
    if zapytanie:
        wyniki = wyniki.filter(numer__icontains=zapytanie)
        
    wyniki = wyniki.order_by('cena')[:5]
    
    return render(request, 'offer/wyszukiwarka.html', {'wyniki': wyniki, 'zapytanie': zapytanie})

from .models import Rejestracja
from django import forms

class RejestracjaForm(forms.ModelForm):
    class Meta:
        model = Rejestracja
        fields = ['imie', 'nazwisko', 'email', 'telefon', 'zgoda_rodo']

def register_view(request, szkolenie_id):
    szkolenie = get_object_or_404(Szkolenie, id=szkolenie_id)
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.szkolenie = szkolenie
            reg.save()
            return render(request, 'offer/success.html')
    else:
        form = RejestracjaForm()
    return render(request, 'offer/register.html', {'form': form, 'szkolenie': szkolenie})

def api_registers(request):
    data = serializers.serialize('json', Rejestracja.objects.all())
    return JsonResponse(data, safe=False)