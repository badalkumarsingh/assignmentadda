from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from .models import Snip
from .forms import snipForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def show_snip(request,link_c):
    snips=Snip.objects.order_by('-updated_at')[:10]
    snip=Snip.objects.get(link_code=link_c)
    return render(request, "snipcode/code.html", {'snip': snip,'snips':snips})

@login_required
def link(request):
    snips=Snip.objects.filter(user=request.user).order_by('-updated_at')[:8]
    return render(request, "snipcode/link.html", {'snips':snips})

@login_required
def delete_snip(request, link_c):
    snip = get_object_or_404(Snip, link_code=link_c)
    if request.method == 'POST':
        form = snipForm(instance=snip, data=request.POST)
        snip.delete()
        return HttpResponseRedirect(reverse('link'))
    else:
        form = snipForm(instance=snip)

    context = {
        'form': form,
        'snip': snip
    }
    return render(request, "snipcode/snip_delete.html", context)

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

def snip(request):
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