# myapp/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def LoadData_info(request):
    if request.method == 'GET':
        LoadData_details = LoadData.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = LoadDataSerializer(LoadData_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def USAStates_info(request):
    if request.method == 'GET':
        USAStates_details = USAStates.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = USAStatesSerializer(USAStates_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def SiteData_info(request):
    if request.method == 'GET':
        SiteData_details = SiteData.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = SiteDataSerializer(SiteData_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def SiteEnviroment_info(request):
    if request.method == 'GET':
        SiteEnviroment_details = SiteEnviroment.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = SiteEnviromentSerializer(SiteEnviroment_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def WasteWater_info(request):
    if request.method == 'GET':
        WasteWater_details = WasteWater.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = WasteWaterSerializer(WasteWater_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def NG_info(request):
    if request.method == 'GET':
        NG_details = NG.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = NGSerializer(NG_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def CrudeOilNodes_info(request):
    if request.method == 'GET':
        CrudeOilNodes_details = CrudeOilNodes.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = CrudeOilNodesSerializer(CrudeOilNodes_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def Users_info(request):
    if request.method == 'GET':
        Users_details = Users.objects.all()
        # NaturalGas_details = NG.objects.latest()
        serializer = UsersSerializer(Users_details, many=True)
        return Response(serializer.data[-1])
        # return Response({"key":"value"})

    elif request.method == 'POST':
        serializer = NGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

