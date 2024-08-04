from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .services import solutioning_generator , persona_profiling_builder , market_analysis_generator
from .models import *
from rest_framework.response import Response
import json

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
    print(projects)
    return render(request, 'myapp/pages/projects.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(StartupProject, id=id)
    print("generated problem :",project.generated_problem )
    if(project.generated_problem is None) : 
        payload = solutioning_generator(project.id, project.startup_name, project.startup_idea)
        project.generated_problem = payload['generated_problem']
        project.generated_slogan = payload['generated_slogan']
        project.generated_solution = payload['generated_solution']
        
    # Save the updated project to the database
        project.save()
    market_analysis = project.generated_market_analysis  
    context = {
        'project': project,
    }
    
    if market_analysis is not None : 
        context['segmentation_data'] =json.dumps({
            'labels': ['Men', 'Women'],
            'datasets': [{
                'data': [
                    market_analysis.market_segmentation_male,
                    market_analysis.market_segmentation_female
                ],
                'backgroundColor': ['#36A2EB', '#FF6384']
            }]
        })
        context['growth_data'] = json.dumps({
            'labels': [ '2020', '2021', '2022', '2023','2024',],
            'datasets': [{
                'label': 'Market Growth',
                'data': [
                    market_analysis.market_growth_1,
                    market_analysis.market_growth_2,
                    market_analysis.market_growth_3,
                    market_analysis.market_growth_4,
                    market_analysis.market_growth_5
                ],
                'backgroundColor': '#ff385c'
            }]
        })
    return render(request, 'myapp/pages/project_detail.html', context)


def chat_view(request):
  return render(request, 'myapp/pages/chat_front.html')


def persona_profiling(request , id):
    project = get_object_or_404(StartupProject, id=id)
    
    if(project.generated_persona is None) : 
        generated_solution =  {
        "generated_slogan":project.generated_slogan,
        "generated_problem":project.generated_problem,
        "generated_solution":project.generated_solution
        }
        persona = persona_profiling_builder(id, generated_solution,project.startup_name, project.startup_idea )
        demographics = persona.get('demographics', {})
        persona = Persona.objects.create(
            demographics_age=demographics['age'],
            demographics_gender=demographics['gender'],
            demographics_location=demographics['location'],
            demographics_occupation=demographics['occupation'],
            demographics_salary=float(demographics['salary']),
            pain_points=persona.get('pain_points', ''),
            core_needs=persona.get('core_needs', ''),
            motivation=persona.get('motivation', ''),
            behavior=persona.get('behavior', ''),
            quote=persona.get('quote', '')
        )
        
        project.generated_persona = persona
        project.save()
        
    market_analysis = project.generated_market_analysis
    
         
    context = {
        'project': project,
    }
    
    if market_analysis is not None : 
        context['segmentation_data'] =json.dumps({
            'labels': ['Men', 'Women'],
            'datasets': [{
                'data': [
                    market_analysis.market_segmentation_male,
                    market_analysis.market_segmentation_female
                ],
                'backgroundColor': ['#36A2EB', '#FF6384']
            }]
        })
        context['growth_data'] = json.dumps({
            'labels': [ '2020', '2021', '2022', '2023','2024',],
            'datasets': [{
                'label': 'Market Growth',
                'data': [
                    market_analysis.market_growth_1,
                    market_analysis.market_growth_2,
                    market_analysis.market_growth_3,
                    market_analysis.market_growth_4,
                    market_analysis.market_growth_5
                ],
                'backgroundColor': '#ff385c'
            }]
        })
        
    return render(request, 'myapp/pages/project_detail.html', context)



def market_analysis_view(request, id) : 
    project = get_object_or_404(StartupProject, id=id)
    generated_solution =  {
        "generated_slogan":project.generated_slogan,
        "generated_problem":project.generated_problem,
        "generated_solution":project.generated_solution
    }
    
    market_analysis_data =market_analysis_generator( project.startup_name , generated_solution)

    market_analysis = MarketAnalysis.objects.create(
        market_size_details=market_analysis_data.get('market_size_details', ''),
        market_size_value=market_analysis_data.get('market_size_value', ''),
        market_segmentation_male=market_analysis_data.get('market_segmentation', {}).get('male', 0),
        market_segmentation_female=market_analysis_data.get('market_segmentation', {}).get('female', 0),
        
        market_growth_1=market_analysis_data.get('market_growth', {}).get('2020', ''),
        market_growth_2=market_analysis_data.get('market_growth', {}).get('2021', ''),
        market_growth_3=market_analysis_data.get('market_growth', {}).get('2022', ''),
        market_growth_4=market_analysis_data.get('market_growth', {}).get('2023', ''),
        market_growth_5=market_analysis_data.get('market_growth', {}).get('2024', ''),
        
        competitor_1=market_analysis_data.get('competitor_list', []).get("1"),
        competitor_2=market_analysis_data.get('competitor_list', []).get("2"),
        competitor_3=market_analysis_data.get('competitor_list', []).get("3"),
        competitor_4=market_analysis_data.get('competitor_list', []).get("4"),
    )
    
    # Link the MarketAnalysis to the project
    project.generated_market_analysis = market_analysis
    project.save()
    
    context = {
        'project': project,
        'segmentation_data': json.dumps({
            'labels': ['Men', 'Women'],
            'datasets': [{
                'data': [
                    market_analysis.market_segmentation_male,
                    market_analysis.market_segmentation_female
                ],
                'backgroundColor': ['#36A2EB', '#FF6384']
            }]
        }),
        'growth_data': json.dumps({
            'labels': [ '2020', '2021', '2022', '2023','2024',],
            'datasets': [{
                'label': 'Market Growth',
                'data': [
                    market_analysis.market_growth_1,
                    market_analysis.market_growth_2,
                    market_analysis.market_growth_3,
                    market_analysis.market_growth_4,
                    market_analysis.market_growth_5
                ],
                'backgroundColor': '#ff385c'
            }]
        })
    }
    
    
    
    return render(request, 'myapp/pages/project_detail.html', context)



def ai_view(request):
    return render(request, 'myapp/pages/ai_front.html')

    
    
    

    





    
    



# def generate(request, id):
#     project = get_object_or_404(StartupProject, id=id)
#     if(project.generated_problem ) : 
#         payload = solutioning_generator(project.id, project.startup_name, project.startup_idea)
#         project.generated_problem = payload['generated_problem']
#         project.generated_slogan = payload['generated_slogan']
#         project.generated_solution = payload['generated_solution']
        
#     # Save the updated project to the database
#         project.save()
    
#     return render(request, 'myapp/pages/project_detail.html',  {'project': project})
