<%
    if defined ("TemplateDefault"):
        setdefault ("Chassis_IndicatorLED", "")
    end
%>
{
  "@Redfish.Copyright": "Copyright 2014-2016 Distributed Management Task Force, Inc. (DMTF). All rights reserved.",
  "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis",
  "@odata.id": "/redfish/v1/Chassis/1",
  "@odata.type": "#Chassis.v1_0_0.Chassis",
  "Id": "1",
  "Name": "Computer System Chassis",
  "ChassisType": "RackMount",
  "Manufacturer": "ManufacturerName",
  "Model": "ProductModelName",
  "SKU": "",
  "SerialNumber": "2M220100SL",
  "PartNumber": "",
  "AssetTag": "CustomerWritableThingy",
  % if defined ("Chassis_IndicatorLED"):
  "IndicatorLED": "{{Chassis_IndicatorLED}}",
  % end
  "PowerState": "On",
  "Status": {
    "State": "Enabled",
    "Health": "OK"
  },
  "Thermal": {
    "@odata.id": "/redfish/v1/Chassis/1/Thermal"
  },
  "Power": {
    "@odata.id": "/redfish/v1/Chassis/1/Power"
  },
  "Links": {
    "ManagedBy": [
      {
        "@odata.id": "/redfish/v1/Managers/1"
      }
    ],
    "ManagersInChassis": [
      {
        "@odata.id": "/redfish/v1/Managers/1"
      }
    ],
    "Oem": {}
  },
  "Oem": {}
}