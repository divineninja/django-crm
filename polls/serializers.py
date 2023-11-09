# polls/serializers.py
from rest_framework import serializers
from .models import Question, Choice, Condition


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class ConditionSerializer(serializers.ModelSerializer):
    parent_answer = ChoiceSerializer(many=True, source='parent_answer.all', read_only=True)

    class Meta:
        model = Condition
        fields = ['question', 'parent_question', 'parent_answer']


class QuestionSerializer(serializers.ModelSerializer):
    conditions = ConditionSerializer(many=True, read_only=True)
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_code', 'order', 'status', 'pub_date', 'conditions', 'choices']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Filter conditions based on the current question
        question_conditions = Condition.objects.filter(parent_question=instance)
        condition_serializer = ConditionSerializer(question_conditions, many=True)

        representation['parent_conditions'] = condition_serializer.data
        return representation
