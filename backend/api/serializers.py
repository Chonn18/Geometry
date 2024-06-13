from rest_framework import serializers
from .model import Problem

class ProblemSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Problem
        fields = ['title','description', 'solve', 'image','image_result','category']
        
    def create(self, validated_data):
        problem = Problem.objects.create(**validated_data)
        return problem

