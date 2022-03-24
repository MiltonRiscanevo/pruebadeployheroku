from rest_framework.serializers import ModelSerializer
from .models import Answers, Question

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        depth = 0

class AnswerSerializer ( ModelSerializer):
    class Meta:
        model: Answers
        fields = '__all__'
        depth = 0