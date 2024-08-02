# Generated by Django 5.0.7 on 2024-08-02 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatbot', models.CharField(choices=[('falcon-180B', 'falcon-180B'), ('falcon-11B', 'falcon-11B')], max_length=20)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('topic', models.CharField(choices=[('ask_doubts', 'Ask doubts'), ('learn_best_practices', 'Learn best practices for building startups'), ('access_previous_qa', 'Access all your previously asked questions and answers'), ('take_quiz', 'Take a quiz to test your knowledge')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(choices=[('user', 'User'), ('chatbot', 'Chatbot')], max_length=7)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='learning_chat.conversation')),
            ],
        ),
    ]
