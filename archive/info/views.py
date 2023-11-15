from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Data saved')
            return redirect('home')
        else:
            form = StudentForm()
    return render(request,'info/home.html',{
        'form':form,
    })

