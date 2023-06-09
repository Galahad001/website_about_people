from rest_framework import serializers
from .models import People
from .models import Category

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'title', 'content', 'images', 'date_create', 'author', 'is_published', 'cat']