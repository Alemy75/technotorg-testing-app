from rest_framework import serializers
from testing.models import Test, Question, Answer, CompletedTest
from django.contrib.auth.models import User


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'name', 'questions']


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name')


class CompletedTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTest
        fields = ('user', 'test', 'score')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')