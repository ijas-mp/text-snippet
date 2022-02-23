from django.shortcuts import render
from rest_framework import permissions
from base.models import textdetails,tagdetails
from base.serializers import textDetailsSerializer,tagDetailsSerializer
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = textdetails.objects.all()
    serializer_class = textDetailsSerializer

class SnippetUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = textdetails.objects.all()
    serializer_class = textDetailsSerializer

class TagList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = tagdetails.objects.all()
    serializer_class = tagDetailsSerializer

# class listtagdetails(APIView):
#     def get(self, request,*k, format=None):
#         print (request)
#         print(k)
#         tesxts = textdetails.objects.filter(tag_id_id=request.pk)
#         serializer = textDetailsSerializer(tesxts, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
def listtagdetails(request,pk):
    if request.method == 'GET':
        tesxts = textdetails.objects.filter(tag_id_id=pk)
        serilizer = textDetailsSerializer(tesxts,many=True)
        return Response(serilizer.data)
