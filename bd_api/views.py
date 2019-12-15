
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config_reader import read_Config
from .models import gate_uid, Gate
from .serializers import GateSerializer, UidSerializer, GateUidSerializer, GateAddSerializer

api_key = read_Config('/app/config.txt', 'api_key')
admin_api_key = read_Config('/app/config.txt', 'admin_api_key')


def check_api_key(request, token):
    Api_Key = request.headers.get('Api-Key')
    if Api_Key is None:
        return False, "Api-Key not found"
    if Api_Key != token:
        return False, "Invalid Api-Key"
    return True, "Access"


@api_view(['GET'])
def get_uids(request):    # получить список user_id привязанных к этому гейту
    flag, message = check_api_key(request, api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    #try:
    gate = request.GET.get('gate_id')
    records = gate_uid.objects.filter(gate_id=gate)
    serializer = UidSerializer(records, many=True)
    return JsonResponse(serializer.data, safe=False)
    # except Exception:
    #     return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_gate(request):     # получить gate к которому привязан user_id
    flag, message = check_api_key(request, api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    try:
        uid = request.GET.get('user_id')
        record = gate_uid.objects.get(user_id=uid)
        serializer = GateSerializer(record)
        return JsonResponse(serializer.data, safe=False)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_new_gates(request):     # добавить новый gate
    flag, message = check_api_key(request, admin_api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    try:
        serializer = GateAddSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])             # связать gate и user_id
def bind(request):
    flag, message = check_api_key(request, api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    try:
        serializer = GateUidSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data['user_id']
            gate = serializer.validated_data['gate_id']
            records = Gate.objects.filter(gate_id=gate)
            if len(records) == 0:
                return Response("This gate does not exist", status=status.HTTP_400_BAD_REQUEST)
            records = gate_uid.objects.filter(user_id=uid)
            if len(records) == 0:
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response("This user_id is already bind", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])             # отвязать user_id от gate
def unbind(request):
    flag, message = check_api_key(request, api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    try:
        gate = request.GET.get("gate_id")
        uid = request.GET.get("user_id")
        record = gate_uid.objects.get(gate_id=gate, user_id=uid)
        record.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def index(request):
    flag, message = check_api_key(request, admin_api_key)
    if not flag:
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    records = Gate.objects.all()
    records2 = gate_uid.objects.all()
    serializer = GateAddSerializer(records, many=True)
    serializer2 = GateUidSerializer(records2, many=True)
    return JsonResponse([serializer.data, serializer2.data], safe=False)
