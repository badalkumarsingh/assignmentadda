from django.shortcuts import render
from .models import Myblog
# Create your views here.
def blog(request):
    blog = Myblog.objects.order_by('date_added')
    context = {'blog': blog}
    return render(request,"blog/index.html", context)

def read(request, blog_id):
    blog = Myblog.objects.get(id=blog_id)
    context = {'blog':blog}
    return render(request, 'blog/read.html', context)