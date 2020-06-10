from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Subject, Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    return render(request, 'assignment_adda/index.html')

def subjects(request):
    subjects = Subject.objects.order_by('date_added')
    context = {'subjects': subjects}
    return render(request, 'assignment_adda/subjects.html', context)
def topics(request, topics_id):
    topic = Subject.objects.get(id=topics_id)
    topicss = topic.topic_set.order_by('date_added')
    context = {'topic':topic, 'topicss':topicss}
    return render(request, 'assignment_adda/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'assignment_adda/topic.html', context)
@login_required
def new_topic(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.subject = subject
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'), args=[subject_id])
    context = {'subject': subject, 'form': form}
    return render(request,'assignment_adda/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.img = form.cleaned_data.get("img") 
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic':topic, 'form': form}
    return render(request,'assignment_adda/new_entry.html', context)
@login_required
def edit_entry(request, edit_id):
    entry = Entry.objects.get(id=edit_id)
    topic = entry.topic
    if entry.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form': form}
    return render(request,'assignment_adda/edit_entry.html', context)
    