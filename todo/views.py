from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task


def index(request):
    if request.method == 'POST':
        date_value = parse_datetime(request.POST['due_at'])
        
        if date_value is not None:
            due_at = make_aware(date_value)
        else:
            due_at = None

        task = Task(title=request.POST['title'], due_at=due_at)
        task.save()

    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')

    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)
