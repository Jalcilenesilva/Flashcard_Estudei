from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.context_processors import request
from .form import TopicForm,EntryForm
from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    """pagina principal"""
    return render(request, 'Estudei/index.html')

@login_required
def topics (request):
    """mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics': topics}
    return render(request, 'Estudei/topics.html',context)

@login_required
def topic (request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    """pagina de erro"""
    if topic.owner !=request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context= {'topic':topic, 'entries':entries}
    return render (request, 'Estudei/topic.html',context)
@login_required
def new_topic(request):
    """Adiciona novo assunto"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()  # Corrigir a indentação aqui
            return HttpResponseRedirect(reverse('topics'))  # Corrigir a indentação aqui

    context = {'form': form}
    return render(request, 'Estudei/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get (id=topic_id)
    """pagina de erro"""
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))

    context ={'topic': topic,'form': form}
    return render(request, 'Estudei/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    """pagina de erro"""
    if topic.owner != request.user:
        raise Http404

    if request.method !='POST':
        """requisição inicial ja tem formularop pronto"""
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'Estudei/edit_entry.html', context)


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    topic.delete()
    return HttpResponseRedirect(reverse('topics'))
@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    entry.delete()
    return HttpResponseRedirect(reverse('topic', args=[topic.id]))
# Create your views here.
