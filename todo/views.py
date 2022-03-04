from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
  
from .models import Todo

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'active_tasks'

    def get_queryset(self):
        return Todo.objects.filter(is_completed=False).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['completed_tasks'] = Todo.objects.filter(is_completed=True).order_by('-date')

        return context

    def post(self, request):

        if "remove" in request.POST:
            task_id = request.POST.get('active_task') 
            if task_id is None:
                return HttpResponseRedirect(reverse('todo:index'))
            task = Todo.objects.get(id = task_id)
            task.delete()
            return HttpResponseRedirect(reverse('todo:index'))
            
        if "remove_completed" in request.POST:
            task_id = request.POST.get('remove_completed')
            if task_id is None:
                return HttpResponseRedirect(reverse('todo:index'))
            task = Todo.objects.get(id = task_id)
            task.delete()
            return HttpResponseRedirect(reverse('todo:index'))

        elif "complete" in request.POST:
            task_id = request.POST.get('active_task')
            if task_id is None:
                return HttpResponseRedirect(reverse('todo:index'))
            task = Todo.objects.get(id = task_id)
            task.is_completed = True
            task.save()
            return HttpResponseRedirect(reverse('todo:index'))

        else:
            return HttpResponseRedirect(reverse('todo:index'))


def add(request):
    task = request.POST.get('new_task')
    new_item = Todo(details = task)
    new_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

