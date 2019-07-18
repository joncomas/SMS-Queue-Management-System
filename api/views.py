from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.queue_datastructure import Queue
import json

# initialize a 'Doe' family
queue = Queue('FIFO')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class QueueView(APIView):
    def get(self, request):
        # fill this method and update the return
        if queue.size() != 0:
            queue.dequeue()
            return Response("Turn was assigned", status=status.HTTP_200_OK)
        else:
            return Response("The list is empty, no need to dequeue", status=status.HTTP_200_OK)

    def post(self, request):
        # add a new member to the queue
        if request is not None:
            queue.enqueue(request)
        return Response(status=status.HTTP_200_OK)

class QueueAllView(APIView):
    def get(self, request):
        # respond a json with all the queue items
        if request.data is not None:
            result = queue.get_all()
        return Response(result, status=status.HTTP_200_OK)