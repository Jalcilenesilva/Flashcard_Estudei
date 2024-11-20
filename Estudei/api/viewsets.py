from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Estudei.models import Topic
from Estudei.api.serializer import TopicSerializer
from rest_framework import status

class TopicViewSets(APIView):
    def get(self, request, id=None):
        if id:
            topic_instance = get_object_or_404(Topic, id=id)
            serializer = TopicSerializer(topic_instance)
            return Response(serializer.data)
        items = Topic.objects.all()
        serializer = TopicSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(selfself, request,id):
        item = get_object_or_404(Topic,id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(selfself, request,id):
        item=get_object_or_404(Topic,id=id)
        serializer= TopicSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)