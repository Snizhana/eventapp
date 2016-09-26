from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from application.models import Application
from events.models import Event
from application.serializers import ApplicationSerializer
import base64


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)

    def create(self, request):
        data = data=request.data
        #data['user_image'] = base64.b64encode(data['user_image'])
        serializer = self.serializer_class(data=data)
        print(request.data)

        if serializer.is_valid():
            serializer.save(event=Event.objects.get(pk=request.data['event_id']))

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        print('ERROR', serializer.errors)
        return Response({
            'status': 'Bad request',
            'message': 'Application could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
