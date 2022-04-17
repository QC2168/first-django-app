import imp
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TodoList
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'list'
    def get_queryset(self):
        return TodoList.objects.all()


def add(request):
    if(request.method=='POST'):
        val=request.POST.get('title')
        if(not val):
            return HttpResponseRedirect( reverse('todolist:index'), {
            'error_message': "标题不能为空.",
        })
        p=TodoList.objects.create(title=val)
        p.save()

    return HttpResponseRedirect(reverse('todolist:index'))


def delete(request):
    if(request.method=='POST'):
        id=request.POST.get('id')
        if(id is None):
            return HttpResponseRedirect( reverse('todolist:index'), {
            'error_message': "ID有误.",
        })
        TodoList.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('todolist:index'))