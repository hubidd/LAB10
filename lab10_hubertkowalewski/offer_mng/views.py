from django.shortcuts import render
from .forms import KategoriaForm, SzkolenieForm

def categ_add(request):
    success = False
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = KategoriaForm() 
    else:
        form = KategoriaForm()
        
    return render(request, 'offer_mng/categ_add.html', {'form': form, 'success': success})

def course_add(request):
    success = False
    if request.method == 'POST':
        form = SzkolenieForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = SzkolenieForm() 
    else:
        form = SzkolenieForm()
        
    return render(request, 'offer_mng/course_add.html', {'form': form, 'success': success})