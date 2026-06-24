from django.shortcuts import render
from django.http import JsonResponse
from .models import Problem  
from .forms import ProblemForm

def problem_report(request):
    success = False 
    
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            success = True
            form = ProblemForm() 
    else:
        form = ProblemForm() 
        
    return render(request, 'issues/problem_report.html', {'form': form, 'success': success})

def api_problems(request):
    problemy = list(Problem.objects.values('id', 'autor', 'temat', 'modul', 'data_zgloszenia'))
    return JsonResponse(problemy, safe=False)