from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import gate_uid
from .serializers import GateSerializer, UidSerializer


@api_view(['GET'])
def get_uids(request, gate):
    if request.method == 'GET':
        try:
            records = gate_uid.objects.filter(gate=gate)
            serializer = UidSerializer(records, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_gate(request, uid):
    if request.method == 'GET':
        try:
            records = gate_uid.objects.filter(uid=uid)
            serializer = GateSerializer(records, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def bind(request, gate="", uid=""):
    print(request.body)
    if request.method == 'POST':
        try:
            gate_uid.objects.get(uid=uid)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            record = gate_uid(gate=gate, uid=uid)
            record.save()
            return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def unbind(request, gate, uid):
    if request.method == 'DELETE':
        try:
            record = gate_uid.objects.get(gate=gate, uid=uid)
            record.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


def index(request):
    return HttpResponse('<h3>старт<h3>')


@api_view(['PUT'])
def sub(request):
    print('I work')
    print(request.path)
    print()
    print(request.method)
    print()
    print(request.body.join())
    return Response(status=status.HTTP_200_OK)
