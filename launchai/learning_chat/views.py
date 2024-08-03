from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import Conversation, Message
# from .serializers import  MessageSerializer
from main.services import generate_completion  
      
class MessageAPIView(APIView):
    def post(self, request, format=None):
        system_prompt = ""
        user_prompt = request.data.get('user_prompt')
        # Generate completion
        response_text = generate_completion(system_prompt, user_prompt)
        
        return Response({
            'message': response_text
        }, status=status.HTTP_200_OK)
