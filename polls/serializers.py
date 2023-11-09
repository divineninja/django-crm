# polls/serializers.py
from rest_framework import serializers
from .models import Question, Choice, Condition


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'parent_question', 'parent_answer']


class QuestionSerializer(serializers.ModelSerializer):
    conditions = ConditionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_code', 'order', 'status', 'pub_date', 'conditions']
