from tkinter.messagebox import RETRY
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET','POST'])
def add_user(request):

    if request.method == 'GET':
      user=User.objects.all()
      serializer = UserSerializer(user, many=True)
      return Response(serializer.data)


    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED )
        return Response(serializer.errors)

    


