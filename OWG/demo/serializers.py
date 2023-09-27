# myapp/serializers.py
from rest_framework import serializers
from .models import *

class LoadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadData
        fields = '__all__'

class USAStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = USAStates
        fields = '__all__'


class SiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteData
        fields = '__all__'

class SiteEnviromentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteEnviroment
        fields = '__all__'

class WasteWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteWater
        fields = '__all__'

class NGSerializer(serializers.ModelSerializer):
    class Meta:
        model = NG
        fields = '__all__'

class CrudeOilNodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudeOilNodes
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
