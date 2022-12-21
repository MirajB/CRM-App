from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import lead
from .forms import leadform
# Create your views here.

def project_homepage(request):
    return render(request,'homepage.html', {})

def app_homepage(request):
    # return HttpResponse("Hi")
    leads = lead.objects.all().order_by('-dt_stamp')
    context = {"leads" : leads}
    print(context)
    return render(request,'leads_homepage.html', context)

def delete_lead(request, pk):
    lead_info = lead.objects.get(id=pk)
    lead_info.delete()
    return redirect("/leads/")

def lead_form(request):
    lform = leadform()
    if request.method == "POST":
        form = leadform(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "form" : lform
    }
    return render(request, "create_lead.html", context)

def update_lead(request, pk):
    
    obj = lead.objects.get(id =pk)
    if request.method == "POST":
        lform = leadform(request.POST, request.FILES, instance=obj)  
        if lform.is_valid():
            lform.save()
    lform = leadform(instance=obj)
    context = {
        "form" : lform,
        "lead" : obj
    }
    return render(request, "update_lead.html", context)