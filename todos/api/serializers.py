from rest_framework import serializers

from todos.models import Todo

class TodosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = '__all__'
