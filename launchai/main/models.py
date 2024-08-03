from django.db import models
from django.contrib.auth.models import User



class Persona(models.Model):
    
    demographics_age = models.IntegerField(null=True)
    demographics_gender = models.BooleanField( null=True)	
    demographics_location = models.CharField(max_length=255 ,null=True)
    demographics_occupation = models.CharField(max_length=255, null=True)
    demographics_salary = models.FloatField(null=True)
    
    pain_points = models.TextField(blank=True, null=True)
    core_needs = models.TextField(blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    
    
class MarketAnalysis(models.Model):
    pass

class StartupProject(models.Model):
    startup_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    startup_idea = models.TextField(blank=True, null=True)
    target_number_of_users_goal = models.IntegerField(blank=True, null=True, default=0)
    target_date_goal = models.DateField(blank=True, null=True)
    
    generated_idea = models.TextField(blank=True, null=True)
    generated_slogan = models.TextField(blank=True, null=True)
    generated_problem = models.TextField(blank=True, null=True)
    generated_solution = models.TextField(blank=True, null=True)
    
    generated_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, blank=True, null=True)
    
    generated_market_analysis = models.OneToOneField(MarketAnalysis, on_delete=models.CASCADE, blank=True, null=True)
    
    generated_mvp_builder = models.TextField(blank=True, null=True)
    generated_user_feedback_analyzer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.startup_name
    

