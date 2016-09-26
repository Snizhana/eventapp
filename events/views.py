from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.shortcuts import get_object_or_404

from events.models import Event
from events.serializers import EventSerializer


@csrf_protect
@ensure_csrf_cookie
def Index(request):
    return render(request, 'index.html')


class EventViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
