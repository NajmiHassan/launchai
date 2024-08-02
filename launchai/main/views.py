from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')



def user_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            # Automatically log the user in after signup
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Account created successfully! You are now logged in.")
                return redirect('set_username')  # Redirect to the home page or any other page after login
            else:
                messages.error(request, "Authentication failed after signup. Please log in manually.")
                return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")

    return render(request, 'myapp/auth/signup.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'myapp/auth/login.html')



@login_required
def set_username(request):
    if request.method == 'POST':
        username = request.POST.get('text')
        if username:
            request.user.username = username
            request.user.save()
            return redirect('set_startup')
    return render(request, 'myapp/pages/welcome.html')

@login_required
def set_startup(request):
    if request.method == 'POST':
        startup_name = request.POST.get('text')
        
        if not startup_name:
            messages.error(request, "Startup name cannot be empty.")
            return redirect('set_startup')
        
        try:
            # Create a new StartupProject with only the startup_name
            project, created = StartupProject.objects.get_or_create(
                user=request.user,
                startup_name=startup_name,
                defaults={
                    'startup_idea': '',
                    'target_number_of_users_goal': 0,
                    'target_date_goal': None
                }
            )
            if not created:
                messages.info(request, "This startup already exists. You can update it.")
            
            request.session['project_id'] = project.id  
            messages.success(request, "Startup successfully set! Now, set your idea.")
            return redirect('set_idea')
        except Exception as e:
            messages.error(request, f"Error setting startup: {e}")

    return render(request, 'myapp/pages/startup_set.html')

@login_required
def set_idea(request):
    project_id = request.session.get('project_id')
    if not project_id:
        messages.error(request, "No startup found. Please set your startup name first.")
        return redirect('set_startup')

    project = get_object_or_404(StartupProject, id=project_id)

    if request.method == 'POST':
        startup_idea = request.POST.get('text')
        
        if not startup_idea:
            messages.error(request, "Startup idea cannot be empty.")
            return redirect('set_idea')
        
        project.startup_idea = startup_idea
        project.save()
        
        messages.success(request, "Startup idea successfully set! Generating dashboard.")
        return redirect('projects')

    return render(request, 'myapp/pages/startup_idea.html')


@login_required
def projects(request):
    # Fetch user's projects
    projects = StartupProject.objects.filter(user=request.user)
    return render(request, 'myapp/pages/projects.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(StartupProject, id=id)
    return render(request, 'myapp/pages/project_detail.html', {'project': project})
