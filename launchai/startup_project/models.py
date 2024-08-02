from django.db import models

# Create your models here.


class StartupProject (models.Model):
    startup_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='projects')
    startup_idea = models.TextField(blank=True, null=True)
    target_number_of_users_goal = models.IntegerField(blank=True, null=True , default=0)
    target_date_goal = models.DateField(blank=True, null=True)
    
    
    generated_idea = models.TextField(blank=True, null=True)
    generated_slogan =  models.TextField(blank=True, null=True)
    generated_problem = models.TextField(blank=True, null=True)
    generated_solution = models.TextField(blank=True, null=True)
    generated_user_persona = models.TextField(blank=True, null=True)
    generated_market_analysis = models.TextField(blank=True, null=True)
    
    
    generated_mvp_builder = models.TextField()
    generated_user_feedback_analyzer = models.TextField()
    
    
    
    
    def __str__(self):
        return self.title