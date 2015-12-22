from django.contrib.auth.models import User, Group
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'description', 'author')

