from rest_framework import serializers
from .models import StartupProject

class StartupProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupProject
        fields = [
            'id',
            'startup_name',
            'created_at',
            'startup_idea',
            'target_number_of_users_goal',
            'target_date_goal',
            'generated_idea',
            'generated_slogan',
            'generated_problem',
            'generated_solution',
            'generated_user_persona',
            'generated_market_analysis'
        ]
        
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }