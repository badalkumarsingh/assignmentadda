from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Snip
from .forms import snipForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404

def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
    return render(request, "snipcode/code.html", {'snip': snip,'snips':snips})

@login_required
def link(request):
    snips=Snip.objects.filter(user=request.user).order_by('-updated_at')[:8]
    return render(request, "snipcode/link.html", {'snips':snips})

@login_required
def edit_snip(request, snip_id):
    snip = Snip.objects.get(link_code=snip_id)
    if request.method != 'POST':
        form = snipForm(instance=snip)
    else:
        form = snipForm(instance=snip, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_snips', args=[snip.link_code]))
    context = {'snip':snip,'form': form}
    return render(request,'snipcode/snip_edit.html', context)

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