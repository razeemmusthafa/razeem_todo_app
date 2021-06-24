from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import task
from . forms import todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django .urls import reverse_lazy
# Create your views here.
class TaskListView(ListView):
    model = task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'i'
    # success_url = reverse_lazy('cbvtask')

class TaskUpdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tasq'
    fields = ('name','priority','date')
    # def get_success_url(self):
    #     return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
    success_url = reverse_lazy('task_view')

class TaskDelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('task_view')

def task_view(request):
    obj1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=task(name=name,priority=priority,date=date)
        obj.save()


    return render(request,'task_view.html',{'obj1':obj1})
#
# def delete(request,taskid):
#     tas=task.objects.get(id=taskid)
#     if request.method=='POST':
#         tas.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'tas':tas})
#
# def update(request,id):
#     tas=task.objects.get(id=id)
#     form=todoforms(request.POST or None,instance=tas)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'edit.html',{'tas':tas,'form':form})
#

