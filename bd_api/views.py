#import django.db.utils.IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import gate_uid, Gate
from .serializers import GateSerializer, UidSerializer, GateUidSerializer, GateAddSerializer

api_key = '32435'

@api_view(['POST'])
def add_gates(request, gate):
    if request.method == 'POST':
        try:
            serializer = GateSerializer(gate)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CRETED) 
        except:
                return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_uids(request):    # получить список user_id привязанных к этому гейту
    try:
        gate = request.GET.get('gate')
        print("get_uids")
        records = gate_uid.objects.filter(gate=gate)
        serializer = UidSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_gate(request):     # получить gate к которому привязан user_id
    try:
        uid = request.GET.get('uid')
        print("get_gate")
        record = gate_uid.objects.get(uid=uid)
        serializer = UidSerializer(record)
        return JsonResponse(serializer.data, safe=False)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_new_gates(request):     # добавить новый gate
    try:
        serializer = GateAddSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])             # связать gate и user_id
def bind(request):
    try:
        serializer = GateUidSerializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data['uid']
            gate = serializer.validated_data['gate']
            records = Gate.objects.filter(gate=gate)
            if len(records) == 0:
                return Response("This gate does not exist", status=status.HTTP_400_BAD_REQUEST)
            records = gate_uid.objects.filter(uid=uid)
            if len(records) == 0:
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response("This user_id is already bind", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])             # отвязать user_id от gate
def unbind(request):
    try:
        gate = request.GET.get("gate")
        uid = request.GET.get("uid")
        print("unbind")
        record = gate_uid.objects.get(gate=gate,uid=uid)
        record.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response("Server feels bad", status=status.HTTP_404_NOT_FOUND)


def index(request):
    records = Gate.objects.all()
    records2 = gate_uid.objects.all()
    serializer = GateAddSerializer(records, many=True)
    serializer2 = GateUidSerializer(records2, many=True)
    return JsonResponse([serializer.data, serializer2.data], safe=False)

# @api_view(['GET'])
# def get_uids(request, gate):
#     if request.method == 'GET':
#         try:
#             records = gate_uid.objects.filter(gate=gate)
#             serializer = UidSerializer(records, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
# #
# # @api_view(['POST'])
# # def set_gates(requsts)
#
# @api_view(['GET'])
# def get_gate(request, uid):
#     if request.method == 'GET':
#         try:
#             records = gate_uid.objects.filter(uid=uid)
#             serializer = GateSerializer(records, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def bind(request, gate="", uid=""):
#     print(request.body)
#     if request.method == 'POST':
#         try:
#             gate_uid.objects.get(uid=uid)
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         except:
#             record = gate_uid(gate=gate, uid=uid)
#             record.save()
#             return Response(status=status.HTTP_200_OK)
#
#
# @api_view(["DELETE"])
# def unbind(request, gate, uid):
#     if request.method == 'DELETE':
#         try:
#             record = gate_uid.objects.get(gate=gate, uid=uid)
#             record.delete()
#             return Response(status=status.HTTP_200_OK)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# def index(request):
#     return HttpResponse('<h3>старт<h3>')
#
#
# @api_view(['PUT'])
# def sub(request):
#     print('I work')
#     print(request.path)
#     print()
#     print(request.method)
#     print()
#     print(request.body.join())
#     return Response(status=status.HTTP_200_OK)
