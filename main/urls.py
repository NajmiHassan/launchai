# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  
    path('login/', views.user_login, name='login'),  
    path('logout/', views.user_login, name='logout'),
    path('set-username/', views.set_username, name='set_username'), 
    path('set_startup/', views.set_startup, name='set_startup'),
    path('set_idea/', views.set_idea, name='set_idea'),
    path('projects/', views.projects, name='projects'), 
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('persona/<int:id>/', views.persona_profiling, name='persona_profiling'),
    path('market/<int:id>/', views.market_analysis_view, name='market_analysis'),
    path('chat/', views.chat_view, name='chat_front'),
    path('ai/', views.ai_view, name='ai_front'),
    path('analyze/', views.analyze_view, name='analyze'),

    # path('project/<int:id>/', views.generate, name='project_detail_generated'),
    
]