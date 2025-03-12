from django.shortcuts import render
from website.models import Contact
from website.forms import NameForm, ContactForm,NewsletterForm
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.name='unknown'
            contact.save()
            
            messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            
            messages.add_message(request,messages.ERROR,'your ticket did not submit')  
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})


def newsletter_view(request):
    if request.method=='POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test.html',{'form':form})


def coming_soon(request):
    return render(request,'coming_soon.html')
    
    

