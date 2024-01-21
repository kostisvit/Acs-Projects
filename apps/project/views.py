from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Project
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'project/home.html')


@login_required
def projects(request):
    projects = Project.objects.filter(author=request.user)

    return render(request, 'project/projects.html', {
        'projects': projects
    })



@login_required
def add(request):
  if request.method == 'POST':
    name = request.POST.get('name', '')
    description = request.POST.get('description', '')

    if name:
      Project.objects.create(name=name, description=description, author=request.user)

      return redirect('/')
    else:
      print('Not valid')

  return render(request, 'project/add.html')
