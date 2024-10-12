from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:             #metaclass describes how a class (outer) behaves
        model = Books
        fields = ['id', 'name', 'type']