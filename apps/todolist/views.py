from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import Todolist
from project.models import Project
from .forms import TodoListForm
from django.utils import timezone

@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(author=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    return render(request, 'todolist/todolist.html', {
        'project': project,
        'todolist': todolist
    })


@login_required
def add(request, project_id):
    project = Project.objects.filter(author=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Todolist.objects.create(project=project, name=name, description=description, author=request.user)

            return redirect(f'/projects/{project_id}/')

    return render(request, 'todolist/add.html', {
        'project': project
    })


@login_required
# def edit(request, project_id, pk):
#     project = Project.objects.filter(author=request.user).get(pk=project_id)
#     todolist = Todolist.objects.filter(project=project).get(pk=pk)

#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         description = request.POST.get('description', '')

#         if name:
#             todolist.name = name
#             todolist.description = description
#             todolist.save()

#             return redirect(f'/projects/{project_id}/{pk}/')

#     return render(request, 'todolist/edit.html', {
#         'project': project,
#         'todolist': todolist
#     })
    

def edit(request,project_id,pk):
    project = Project.objects.filter(author=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    instance = get_object_or_404(Todolist,pk=pk)
    if request.method == 'POST':
        form = TodoListForm(request.POST,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.completion_date = timezone.now().date()
            instance.save()
            print('Project created')
            return redirect('/')
    else:
        form=TodoListForm(instance=instance)
    return render(request, 'project/edit.html', {'project': project,
        'todolist': todolist,'form': form})


@login_required
def delete(request, project_id, pk):
    project = Project.objects.filter(author=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    todolist.delete()

    return redirect(f'/projects/{project_id}/')



