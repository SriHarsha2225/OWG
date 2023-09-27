import os
from datetime import time
from django.apps import apps
import paho.mqtt.client as mqtt
from django.conf import settings
import json
# from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from . import multi_topic_file
# import ssl

print('mqtt')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Automac_main.settings')


def on_connect(client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully on hive')
       client.subscribe('LoadData_info')
       client.subscribe('USAStates_info')
       client.subscribe('SiteData_info')
       client.subscribe('SiteEnviroment_info')
       client.subscribe('WasteWater_info')
       client.subscribe('NG_info')
       client.subscribe('CrudeOilNodes_info')
       client.subscribe('Users_info')

   else:
       print('Bad connection. Code:', rc)

def on_message(client, userdata, msg):
    print("on_message")
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload.decode("utf-8")}')
    data1 = str(msg.payload.decode("utf-8"))
    data = json.loads(data1)
    print(type(data))
    print()
    if msg.topic == 'LoadData_info':
        print('LoadData_info')
        from .models import LoadData
        new_data = LoadData(BillOfLading_Load_Id=data['BillOfLading_Load_Id'],
                            Load_Ready=data['Load_Ready'],
                            Load_Pick_Up_Address=data['Load_Pick_Up_Address'],
                            Load_Drop_Off_Address=data['Load_Drop_Off_Address'],
                            Load_Medium=data['Load_Medium'],
                            Medium_Tank_Id=data['Medium_Tank_Id'],
                            Pick_Up_Time=data['Pick_Up_Time'],
                            Pick_Up_Scheduled_Date=data['Pick_Up_Scheduled_Date'],
                            Pick_Up_Load_Price=data['Pick_Up_Load_Price'],
                            Motor_Carrier_Number=data['Motor_Carrier_Number'],
                            Pick_Up_Distance=data['Pick_Up_Distance'],
                            Drop_Off_Distance=data['Drop_Off_Distance'],
                            Estimated_Pick_Up_Fuel=data['Estimated_Pick_Up_Fuel'],
                            Estimated_Drop_Off_Fuel=data['Estimated_Drop_Off_Fuel'],
                            Comfirm_Pick_Up=data['Comfirm_Pick_Up'],
                            Comfirm_Drop_Off=data['Comfirm_Drop_Off'],
                            Drop_Off_Reciept=data['Drop_Off_Reciept'],
                            Drop_Off_Time_Date=data['Drop_Off_Time_Date'],
                            Driver_Pay=data['Driver_Pay']
                            )
        new_data.save()
    if msg.topic == 'USAStates_info':
        print('USAStates_info')
        from .models import USAStates
        new_data = USAStates(State_Name=data['State_Name'],
                            State_Zip=data['State_Zip'],

                            )
        new_data.save()
    if msg.topic == 'SiteData_info':
        print('SiteData_info')
        from .models import SiteData
        new_data = SiteData(Site_Environment=data['Site_Environment'],
                            Crude_Oil_Tanks=data['Crude_Oil_Tanks'],
                            Natural_Gas_Tanks=data['Natural_Gas_Tanks'],
                            Natural_Gas_Pipe_ransfer=data['Natural_Gas_Pipe_ransfer'],
                            Natural_Gas_BurnOff=data['Natural_Gas_BurnOff'],
                            Waster_Water=data['Waster_Water'],
                            USA_State_Name=data['USA_State_Name'],
                            Site_Address=data['Site_Address']
                            )
        new_data.save()
    if msg.topic == 'SiteEnviroment_info':
        print('SiteEnviroment_info')
        from .models import SiteEnviroment
        new_data = SiteEnviroment(Site_ID=data['Site_ID'],
                            Site_Temp_Node=data['Site_Temp_Node'],
                            Site_Pressure_Node=data['Site_Pressure_Node'],
                            Site_Rain_Pressure_Node=data['Site_Rain_Pressure_Node'],
                            Site_H2S_Sensor_Node=data['Site_H2S_Sensor_Node'],
                            Site_Combustible_Gas_Node=data['Site_Combustible_Gas_Node'],
                            Site_Microphone_Node=data['Site_Microphone_Node'],
                            Site_Fire_Alert_Node=data['Site_Fire_Alert_Node'],
                            Site_Fire_Robot_Water_Usage_Node=data['Site_Fire_Robot_Water_Usage_Node'],
                            Site_Explosion_Proof_Fan_Switch_Node=data['Site_Explosion_Proof_Fan_Switch_Node'],
                            Site_Fire_Fighter_Robot_Activation_Node=data['Site_Fire_Fighter_Robot_Activation_Node']
                            )
        new_data.save()
    if msg.topic == 'WasteWater_info':
        print('WasteWater_info')
        from .models import WasteWater
        new_data = WasteWater(Waste_Water_Tank_Temp_Node=data['Waste_Water_Tank_Temp_Node'],
                            Waste_Water_Tank_Pressure_Nodes=data['Waste_Water_Tank_Pressure_Nodes'],
                            Waste_Water_Pick_Up_Temp_Node=data['Waste_Water_Pick_Up_Temp_Node'],
                            Waste_Water_Pick_Up_Valve_Node=data['Waste_Water_Pick_Up_Valve_Node'],
                            Waste_Water_Pick_Up_Visco_Node=data['Waste_Water_Pick_Up_Visco_Node'],
                            Waste_Water_Tank_Level_Node=data['Waste_Water_Tank_Level_Node'],
                            Medium_Waste_Water=data['Medium_Waste_Water'],
                            )
        new_data.save()
    if msg.topic == 'NG_info':
        print('NG_info')
        from .models import NG
        new_data = NG(Natural_Gas_Tank_Temp_Node=data['Natural_Gas_Tank_Temp_Node'],
                            Natural_Gas_Diff_Pressure_Node=data['Natural_Gas_Diff_Pressure_Node'],
                            Natural_Gas_Tank_Pressure_Node=data['Natural_Gas_Tank_Pressure_Node'],
                            Natural_Gas_Tank_Level_Node=data['Natural_Gas_Tank_Level_Node'],
                            Natural_Gas_Pick_Up_Valve_Node=data['Natural_Gas_Pick_Up_Valve_Node'],
                            Vortex_Flow_Metering_Unit_Node=data['Vortex_Flow_Metering_Unit_Node'],
                            Natural_Gas_Pick_Up_Temp_Node=data['Natural_Gas_Pick_Up_Temp_Node'],
                            Medium_Natural_Gas=data['Medium_Natural_Gas']
                            )
        new_data.save()
    if msg.topic == 'CrudeOilNodes_info':
        print('CrudeOilNodes_info')
        from .models import CrudeOilNodes
        new_data = CrudeOilNodes(Site_ID=data['Site_ID'],
                            Oil_Tank_Temp_Node=data['Oil_Tank_Temp_Node'],
                            Oil_Tank_Water_Visco_Drain_Node=data['Oil_Tank_Water_Visco_Drain_Node'],
                            Oil_Tank_Visco_Drain_Node=data['Oil_Tank_Visco_Drain_Node'],
                            Oil_Tank_Pressure_Node=data['Oil_Tank_Pressure_Node'],
                            Oil_Tank_Waste_Water_Valve=data['Oil_Tank_Waste_Water_Valve'],
                            Oil_Tank_Pick_Up_Temp_Nodes=data['Oil_Tank_Pick_Up_Temp_Nodes'],
                            Oil_Tank_Pick_Up_Visco_Node=data['Oil_Tank_Pick_Up_Visco_Node'],
                            Oil_Tank_Pick_Up_Valve_Node=data['Oil_Tank_Pick_Up_Valve_Node'],
                            Oil_Tank_Pick_Up_Flow_Node=data['Oil_Tank_Pick_Up_Flow_Node'],
                            Medium_Crude_Oil=data['Medium_Crude_Oil']
                            )
        new_data.save()
    if msg.topic == 'Users_info':
        print('Users_info')
        from .models import Users
        new_data = Users(Name=data['Name'],
                            Email=data['Email'],
                            Phone_Number=data['Phone_Number'],
                            User_Type=data['User_Type'],
                            Insurance=data['Insurance'],
                            Background_Check=data['Background_Check'],
                            Driving_Record=data['Driving_Record'],
                            Motor_Carrier_Number=data['Motor_Carrier_Number'],
                            USA_State=data['USA_State'],
                            Activity_Log=data['Activity_Log'],
                            DriverPreferedDistance=data['DriverPreferedDistance']
                            )
        new_data.save()


    # mqtt_machines_data = msg.payload.decode()  # Assuming the payload is a string
    # payload_json = json.loads(mqtt_machines_data)
    # topic=msg.topic
    # print('mqtt_machines_data',msg.topic)
    # print('timestamp :', payload_json['timestamp'])
    # print('machineid :', payload_json['info']['mid'])

    # multi_topic_file.all_topics(mqtt_machines_data,topic)

    # if topic =='maithri/abu_dabhi' or topic =='Topic_name':
        # from . import physical_keys_values
        # physical_keys_values.mqtt_data_to_channels(mqtt_machines_data)

    # else:
    #     pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
   host='broker.hivemq.com',
   port=1883,
   keepalive=60
)