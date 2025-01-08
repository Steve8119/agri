from django.shortcuts import render
from .gemini_service import diagnose_problem

def diagnose(request):
    diagnosis = ""
    if request.method == "POST":
        problem_description = request.POST.get("problem_description")
        diagnosis = diagnose_problem(problem_description)
    return render(request, "diagnosis/diagnose.html", {"diagnosis": diagnosis})
