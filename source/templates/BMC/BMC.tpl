{
  "@Redfish.Copyright": "Copyright 2014-2016 Distributed Management Task Force, Inc. (DMTF). All rights reserved.",
  "@odata.context": "/redfish/v1/$metadata#Manager.Manager",
  "@odata.id": "/redfish/v1/Managers/1",
  "@odata.type": "#Manager.v1_0_0.Manager",
  "Id": "1",
  "Name": "Manager",
  "ManagerType": "BMC",
  "Description": "BMC",
  "ServiceEntryPointUUID": "92384634-2938-2342-8820-489239905423",
  "UUID": "00000000-0000-0000-0000-000000000000",
  "Model": "AST2520",
  "DateTime": "2015-03-13T04:14:33+06:00",
  "DateTimeLocalOffset": "+06:00",
  "Status": {
    "State": "Enabled",
    "Health": "OK"
  },
  "GraphicalConsole": {
    "ServiceEnabled": false,
    "MaxConcurrentSessions": 0,
    "ConnectTypesSupported": [
      "None"
    ]
  },
  "SerialConsole": {
    "ServiceEnabled": true,
    "MaxConcurrentSessions": 1,
    "ConnectTypesSupported": [
      "Telnet",
      "SSH"
    ]
  },
  "CommandShell": {
    "ServiceEnabled": true,
    "MaxConcurrentSessions": 4,
    "ConnectTypesSupported": [
      "Telnet",
      "SSH"
    ]
  },
  "FirmwareVersion": "1.00",
  "NetworkProtocol": {
    "@odata.id": "/redfish/v1/Managers/1/NetworkProtocol"
  },
  "EthernetInterfaces": {
    "@odata.id": "/redfish/v1/Managers/1/EthernetInterfaces"
  },
  "SerialInterfaces": {
    "@odata.id": "/redfish/v1/Managers/1/SerialInterfaces"
  },
  "LogServices": {
    "@odata.id": "/redfish/v1/Managers/1/LogServices"
  },
  "Links": {
    "ManagerForServers": [
      {
        "@odata.id": "/redfish/v1/Systems/1"
      }
    ],
    "ManagerForChassis": [
      {
        "@odata.id": "/redfish/v1/Chassis/1"
      }
    ],
    "ManagerInChassis": {
      "@odata.id": "/redfish/v1/Chassis/1"
    },
    "Oem": {}
  },
  "Actions": {
    "#Manager.Reset": {
      "target": "/redfish/v1/Managers/1/Actions/Manager.Reset",
      "ResetType@Redfish.AllowableValues": [
        "ForceRestart",
        "GracefulRestart"
      ]
    },
    "Oem": {}
  },
  "Oem": {}
}
