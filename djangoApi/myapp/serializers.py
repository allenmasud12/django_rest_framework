from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    title = serializers.CharField()


    def create(self, validated_data):
        return Contact.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)

        instance.save()
        return instance