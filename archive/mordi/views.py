from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView
from .forms import StaffForm, PublicationForm,ConferenceForm,BookForm,PromotionForm,searchform,UserForm,UserProfile
from django.contrib import messages
from django.contrib.auth.models import AbstractUser, User
#from .forms import ModelFormWithFileField
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import  get_object_or_404

# Create your views here.

def modric(request):
    everyone = Staff.objects.all()
    number = Staff.objects.count()
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            messages.success(request,f'Data saved')
            return redirect("journal")
    else:
        form = StaffForm()
    return render(request, "mordi/upload.html", {"form": form,'everyone':everyone,'number':number,'check':1})


def journal(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            
            obj.user = get_object_or_404(Staff, pk=request.user.id)
            obj.save()
            
            messages.success(request,f'Publication saved saved')
            return redirect("conference")
    else:
        form = PublicationForm()
    return render(request, "mordi/gene_form.html", {"form": form, 'tit':'Journal','tits':'mordi/pubform.html','home':'conference'})


def conference(request):
    print(Staff.objects.get(pk=request.user.id))
    if request.method == "POST":
        form = ConferenceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = Staff.objects.get(pk=request.user.id)
            obj.save()
            
            messages.success(request,f'Conference Info saved saved')
            return redirect("book")
    else:
        form = ConferenceForm()
    return render(request, "mordi/gene_form.html", {"form": form, 'tit':'Conference','tits':'mordi/conform.html','home':'book'})


def book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = Staff.objects.get(pk=request.user.id)
            obj.save()
            messages.success(request,f'Book Info saved saved')
            return redirect("promotion")
    else:
        form = BookForm()
    return render(request, "mordi/gene_form.html", {"form": form, 'tit':'book','tits':'mordi/bookform.html','home':'promotion'})


def promo(request):
    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = Staff.objects.get(pk=request.user.id)
            obj.save()
            messages.success(request,f'Promotion data saved')
            return redirect("endpage")
    else:
        form = PromotionForm()
    return render(request, "mordi/gene_form.html", {"form": form, 'tit':'Promotion','tits':'mordi/promoform.html', 'home':'home'})


def seeker(request):
    everyone = Staff.objects.all()
    number = Staff.objects.count()
    curious =searchform()
    print('here')
    if request.method == "POST":
        print('yes')
        
        pub= request.POST.get('pub_number')
        confe = request.POST.get('conf_number')
        boo = request.POST.get('book_number')
        
        emp=Staff.objects.annotate(
            publi = models.Count('publication'),
            confee = models.Count('conference'),
            bookss=models.Count('book')
        ).filter(
            publi__gte = pub,
            confee__gte = confe,
            bookss__gte = boo
        )
        print(emp)
        print('****************')
        print(boo)
        context = {
            'emp':emp,
            'curious':curious,
            'everyone':everyone,
            'number':number
            
            
        }
        return render(request,'mordi/upload.html',context)
    return render(request,"mordi/upload.html",{'curious':curious,'everyone':everyone,
            'number':number})

@login_required(login_url='login')
def update_staff(request):
    everyone = Staff.objects.all()
    number = Staff.objects.count()
    if request.method == 'POST':
        print(request.user)
        user_form = UserProfile(request.POST, instance=request.user)
        form = StaffForm(request.POST,  request.FILES,instance=request.user.staff)
        user=User.objects.get(username=request.user)
        
        
        print(form.is_valid())
        if  form.is_valid() and user_form.is_valid():
            
            form.save()
            user_form.save()
            # person = User.objects.get(username=request.user)
            # obj.user = person
            # obj.save()
            messages.success(request, ('Your Staff profile was successfully updated!'))
            return redirect('journal')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserProfile(instance=request.user)
        form = StaffForm(instance=request.user.staff)
    return render(request, "mordi/profile.html", {
        
        'form': form,
        'everyone':everyone,
        'number':number,
        'check':1,
        'user_form':user_form
    })

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            individual = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Hello {username}, your account has been created, go ahead fill this form')
            login(request,individual)
            return redirect('update_staff')
    else:
        form = UserForm()
    return render(request,'register.html',{'form':form})



class PublicationCreateView(CreateView):
    model = Publication
    template_name = "mordi/gene_form.html"
    form_class = PublicationForm
    success_url = reverse_lazy('conference')

    # def get_initial(self):
    #     initial = super(PublicationCreateView,self).get_initial()
    #     initial['user']= Staff.objects.get(pk=self.kwargs['pk'])
    #     print(initial)
    #     return initial
    
    def form_valid(self, form,**kwargs):
        obj = form.save(commit=False)
        obj.user = Staff.objects.get(request.user.id)
        obj.save()
        return HttpResponseRedirect(self.success_url)
    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'tit':'Journal',
            'tits':'mordi/pubform.html',
            'home':'conference'
        })
        return context

def endpage(request):
    date = datetime.date.today()
    return render(request,'mordi/end.html',{'date':date.year})


def profile(request):
    person = Staff.objects.get(user=request.user)
    # dd = get_object_or_404(Publication, user=request.user.staff)
    pubs = Publication.objects.filter(user = request.user.staff)
    cons = Conference.objects.filter(user = request.user.staff)
    books = Book.objects.filter(user = request.user.staff)
    promos = Promotion.objects.filter(user = request.user.staff)
    
    context ={
        'person':person,
        'pubs':pubs,
        'cons':cons,
        'books':books,
        'promos':promos,
        'hope':1,
        'tit':f"{person}'s Profile",'tits':'mordi/sketch.html', 'home':'home'
    }
    return render(request,'mordi/gene_form.html',context)

