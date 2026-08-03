from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import members
from .forms import abc
# Create your views here.
def home(request):
    return HttpResponse("<b>Hello, World!<?b><h1>Heading tag</h1>")
def home2(request):
    return render(request,"index.html")
def home3(request):
    parrot={
        "name": "Anu",
        "number": 49,
        "no": 8019324187

    }
    return render(request,"demo.html", parrot)

def home4(request):
    value=members.objects.all()
    context={
        'key':value
    }
    return render(request,'members.html',context)
def home5(request):
    if request.method == 'POST':
        value = abc(request.POST)
        if value.is_valid():
            value.save()
            return redirect('members-list')
    else:
        value = abc()

    content = {
        'key': value
    }

    return render(request, 'auto_fields.html', content)