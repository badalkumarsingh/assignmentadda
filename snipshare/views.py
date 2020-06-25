from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm
from django.contrib.auth.decorators import login_required

def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
    return render(request, "snipcode/code.html", {'snip': snip,'snips':snips})

@login_required
def link(request):
    snips=Snip.objects.filter(user=request.user).order_by('-updated_at')[:8]
    return render(request, "snipcode/link.html", {'snips':snips})

def index(request):
    snips=Snip.objects.order_by('-updated_at')[:8]
    form=snipForm(request.POST)
    if request.method =='POST':
        if form.is_valid(): 
            obj = form.save(commit = False) 
            obj.user = request.user; 
            obj.save() 
            form = snipForm()
            return HttpResponseRedirect("mylinks") 
        else:
            form = snipForm()
    return render(request, "snipcode/index.html", {'form':form, 'snips':snips})