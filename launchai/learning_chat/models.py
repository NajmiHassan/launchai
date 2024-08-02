from django.db import models

# from users.models import User

# Create your models here.


class Conversation(models.Model):
    
    CHATBOT_CHOICES = [
        ("falcon-180B", 'falcon-180B'),
        ("falcon-11B", 'falcon-11B'),
    ]
    
    ASK_DOUBTS = 'ask_doubts'
    LEARN_BEST_PRACTICES = 'learn_best_practices'
    ACCESS_PREVIOUS_QA = 'access_previous_qa'
    TAKE_QUIZ = 'take_quiz'

    TOPIC_CHOICES = [
        (ASK_DOUBTS, 'Ask doubts'),
        (LEARN_BEST_PRACTICES, 'Learn best practices for building startups'),
        (ACCESS_PREVIOUS_QA, 'Access all your previously asked questions and answers'),
        (TAKE_QUIZ, 'Take a quiz to test your knowledge'),
    ]
    # user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='conversations')
    chatbot = models.CharField(max_length=20, choices=CHATBOT_CHOICES)
    started_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64, blank=True, null=True) 
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)



class Message(models.Model):
    USER = 'user'
    CHATBOT = 'chatbot'

    SENDER_CHOICES = [
        (USER, 'User'),
        (CHATBOT, 'Chatbot'),
    ]
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=7, choices=SENDER_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)