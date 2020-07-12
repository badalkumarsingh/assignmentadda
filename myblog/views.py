from django.shortcuts import render
from .models import Myblog
from .forms import CommentForm
from rest_framework import generics
from .serializers import MyblogSerializer

class MyblogViewSet(generics.ListAPIView):
    queryset = Myblog.objects.all().order_by('date_added')
    serializer_class = MyblogSerializer

def blog(request):
    blog = Myblog.objects.order_by('date_added')
    context = {'blogs': blog,'read_more':' Read More...'}
    return render(request,"blog/index.html", context)

def read(request, blog_title):
    blog = Myblog.objects.get(title=blog_title)
    comments = blog.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'blog': blog,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form}
    return render(request, 'blog/read.html', context)