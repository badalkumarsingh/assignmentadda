from django.shortcuts import render
from .models import Myblog
from .forms import CommentForm
# Create your views here.
def blog(request):
    blog = Myblog.objects.order_by('date_added')
    context = {'blog': blog}
    return render(request,"blog/index.html", context)

def read(request, blog_title):
    blog = Myblog.objects.get(title=blog_title)
    comments = blog.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'blog': blog,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form}
    return render(request, 'blog/read.html', context)