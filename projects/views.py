from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.urlresolvers import resolve
from django.contrib.auth.decorators import login_required
from .models import Project
from tasks.models import Task
from accounts.models import UserProfile
from .forms import ProjectForm

# Create your views here.
@login_required()
#Get all Projects
def get_projects(request):
    
       #Check if user used the select option
    if request.method == "POST":

        """ 
        This is for the filtered select option
        on the tasks page
        """
        search_select = request.POST['search']

        if search_select == 'all':
            projects = Project.objects.filter(user__username=request.user)
        
        if search_select == 'work':
            projects = Project.objects.filter(status='Work', user__username=request.user)

        if search_select == 'education':
            projects = Project.objects.filter(status='Education', user__username=request.user)
            
        if search_select == 'personal':
            projects = Project.objects.filter(status='Personal', user__username=request.user)
            
        """ 
        What ever is choosen in the select box 
        is no filtered and resend to tasks page
        """
        return render(request, "projects.html", {'projects': projects})
        
    else:
        projects = Project.objects.filter(user__username=request.user)
        
        return render(request, "projects.html", {'projects': projects})
        
        
@login_required()    
#Get Project Information
def project_info(request, pk):
    
    project = get_object_or_404(Project, pk=pk)
    project.save()
    
    user_info = UserProfile.objects.filter(user=request.user)
    
    for u in user_info:
        picture = u.picture
    
    return render(request, "projectinfo.html", {
        'project': project,
        'picture': picture
    })
    
@login_required()  
#Edit or Create a Project
def create_or_edit_project(request, pk=None):
    
    project_count = 0
    account_type = ""
    
    info = UserProfile.objects.filter(user=request.user)
    for i in info:
        account_type = i.account
        
    projects = Project.objects.filter(user__username=request.user)

    for p in projects:
        project_count = project_count + 1

    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == "POST":
        
        if account_type == "free" and project_count >= 1 and pk == None:

            return render(request,'projects.html',{
                'projects': projects,
                'result': "trial"
            })
        else:

            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                return redirect(reverse('project_info', kwargs={
                    'pk': project.id 
                }))
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projectform.html', {
        'form': form,
        'project': pk
    })
    
    
@login_required()   
#Deletes a project
def delete_project(request, pk=None):
    
    Project.objects.filter(id=pk).delete()
    return redirect(reverse('get_projects'))
    

@login_required()
#Selects tasks for a specific project only
def view_only(request, pk=None):

    project = Project.objects.filter(id=pk)
    tasks = Task.objects.filter(project=project)
    
    for p in project:
        project_name = p.name
        
    #Check if user used the select option
    if request.method == "POST":

        """ 
        This is for the filtered select option
        on the tasks page
        """
        search_select = request.POST['search']
        
        if search_select == 'all':
            tasks = Task.objects.filter(project=project)

        if search_select == 'hpriority':
            tasks = Task.objects.filter(priority='High', project=project)

        if search_select == 'mpriority':
            tasks = Task.objects.filter(priority='Medium', project=project)

        if search_select == 'lpriority':
            tasks = Task.objects.filter(priority='Low', project=project)

        if search_select == 'todo':
            tasks = Task.objects.filter(status='To Do', project=project)

        if search_select == 'progress':
            tasks = Task.objects.filter(status='In Progress', project=project)

        if search_select == 'done':
            tasks = Task.objects.filter(status='Done', project=project)

        """ 
        What ever is choosen in the select box 
        is no filtered and resend to tasks page
        """
        return render(request, "project_tasks.html", {
            'tasks': tasks,
            'project_id': pk,
            'project': project_name
        })
        
    else:
        tasks = Task.objects.filter(project=project)
        return render(request, "project_tasks.html", {
            'tasks': tasks,
            'project_id': pk,
            'project': project_name
        })    

