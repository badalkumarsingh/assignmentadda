from django.shortcuts import render
from .models import Myblog
# Create your views here.
def blog(request):
    blog = Myblog.objects.order_by('date_added')
    context = {'blog': blog}
    return render(request,"blog/index.html", context)

def read(request, blog_title):
    blog = Myblog.objects.get(title=blog_title)
    context = {'blog':blog}
    return render(request, 'blog/read.html', context)