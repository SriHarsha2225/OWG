# myapp/models.py
from django.db import models



class LoadData(models.Model):
    BillOfLading_Load_Id = models.CharField(max_length=255)
    Load_Ready = models.CharField(max_length=255)
    Load_Pick_Up_Address = models.CharField(max_length=255)
    Load_Drop_Off_Address = models.CharField(max_length=255)
    Load_Medium = models.CharField(max_length=255)
    Medium_Tank_Id = models.CharField(max_length=255)
    Pick_Up_Time = models.CharField(max_length=255)
    Pick_Up_Scheduled_Date = models.CharField(max_length=255)
    Pick_Up_Load_Price = models.CharField(max_length=255)
    Motor_Carrier_Number = models.CharField(max_length=255)
    Pick_Up_Distance = models.CharField(max_length=255)
    Drop_Off_Distance = models.CharField(max_length=255)
    Estimated_Pick_Up_Fuel = models.CharField(max_length=255)
    Estimated_Drop_Off_Fuel = models.CharField(max_length=255)
    Comfirm_Pick_Up = models.CharField(max_length=255)
    Comfirm_Drop_Off = models.CharField(max_length=255)
    Drop_Off_Reciept = models.CharField(max_length=255)
    Drop_Off_Time_Date = models.CharField(max_length=255)
    Driver_Pay = models.CharField(max_length=255)




class USAStates(models.Model):
    State_Name = models.CharField(max_length=255)
    State_Zip = models.CharField(max_length=255)



class SiteData(models.Model):
    Site_Environment = models.CharField(max_length=255)
    Crude_Oil_Tanks = models.CharField(max_length=255)
    Natural_Gas_Tanks = models.CharField(max_length=255)
    Natural_Gas_Pipe_ransfer = models.CharField(max_length=255)
    Natural_Gas_BurnOff = models.CharField(max_length=255)
    Waster_Water = models.CharField(max_length=255)
    USA_State_Name = models.CharField(max_length=255)
    Site_Address = models.CharField(max_length=255)



class SiteEnviroment(models.Model):
    Site_ID = models.CharField(max_length=255)
    Site_Temp_Node = models.CharField(max_length=255)
    Site_Pressure_Node = models.CharField(max_length=255)
    Site_Rain_Pressure_Node = models.CharField(max_length=255)
    Site_H2S_Sensor_Node = models.CharField(max_length=255)
    Site_Combustible_Gas_Node = models.CharField(max_length=255)
    Site_Microphone_Node = models.CharField(max_length=255)
    Site_Fire_Alert_Node = models.CharField(max_length=255)
    Site_Fire_Robot_Water_Usage_Node = models.CharField(max_length=255)
    Site_Explosion_Proof_Fan_Switch_Node = models.CharField(max_length=255)
    Site_Fire_Fighter_Robot_Activation_Node = models.CharField(max_length=255)


class WasteWater(models.Model):
    Waste_Water_Tank_Temp_Node = models.CharField(max_length=255)
    Waste_Water_Tank_Pressure_Nodes = models.CharField(max_length=255)
    Waste_Water_Pick_Up_Temp_Node = models.CharField(max_length=255)
    Waste_Water_Pick_Up_Valve_Node = models.CharField(max_length=255)
    Waste_Water_Pick_Up_Visco_Node = models.CharField(max_length=255)
    Waste_Water_Tank_Level_Node = models.CharField(max_length=255)
    Medium_Waste_Water = models.CharField(max_length=255)


class NG(models.Model):
    Natural_Gas_Tank_Temp_Node = models.CharField(max_length=255)
    Natural_Gas_Diff_Pressure_Node = models.CharField(max_length=255)
    Natural_Gas_Tank_Pressure_Node = models.CharField(max_length=255)
    Natural_Gas_Tank_Level_Node = models.CharField(max_length=255)
    Natural_Gas_Pick_Up_Valve_Node = models.CharField(max_length=255)
    Vortex_Flow_Metering_Unit_Node = models.CharField(max_length=255)
    Natural_Gas_Pick_Up_Temp_Node = models.CharField(max_length=255)
    Medium_Natural_Gas = models.CharField(max_length=255)


class CrudeOilNodes(models.Model):
    Site_ID = models.CharField(max_length=255)
    Oil_Tank_Temp_Node = models.CharField(max_length=255)
    Oil_Tank_Water_Visco_Drain_Node = models.CharField(max_length=255)
    Oil_Tank_Visco_Drain_Node = models.CharField(max_length=255)
    Oil_Tank_Pressure_Node = models.CharField(max_length=255)
    Oil_Tank_Waste_Water_Valve = models.CharField(max_length=255)
    Oil_Tank_Pick_Up_Temp_Nodes = models.CharField(max_length=255)
    Oil_Tank_Pick_Up_Visco_Node = models.CharField(max_length=255)
    Oil_Tank_Pick_Up_Valve_Node = models.CharField(max_length=255)
    Oil_Tank_Pick_Up_Flow_Node = models.CharField(max_length=255)
    Medium_Crude_Oil = models.CharField(max_length=255)


class Users(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=255)
    User_Type = models.CharField(max_length=255)
    Insurance = models.CharField(max_length=255)
    Background_Check = models.CharField(max_length=255)
    Driving_Record = models.CharField(max_length=255)
    Motor_Carrier_Number = models.CharField(max_length=255)
    USA_State = models.CharField(max_length=255)
    Activity_Log = models.CharField(max_length=255)
    DriverPreferedDistance = models.CharField(max_length=255)

