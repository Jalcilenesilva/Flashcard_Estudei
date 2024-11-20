from rest_framework import serializers
from Estudei import models

class TopicSerializer (serializers.ModelSerializer):
    class Meta:
        model= models.Topic
        fields = '__all__'