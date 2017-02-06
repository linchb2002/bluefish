{

  "@Redfish.Copyright": "Copyright 2014-2016 Distributed Management Task Force, Inc. (DMTF). All rights reserved.",

  "@odata.context": "/redfish/v1/$metadata#Power.Power",

  "@odata.id": "/redfish/v1/Chassis/1/Power",

  "@odata.type": "#Power.v1_1_0.Power",

  "Id": "Power",

  "Name": "Power",


  "Voltages": [

    {

      "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/0",

      "MemberId": "0",

      "Name": "VRM1 Voltage",

      "SensorNumber": 11,

      "Status": {

        "State": "Enabled",

        "Health": "OK"

      },

      "ReadingVolts": 12,

      "UpperThresholdNonCritical": 12.5,

      "UpperThresholdCritical": 13,

      "UpperThresholdFatal": 15,

      "LowerThresholdNonCritical": 11.5,

      "LowerThresholdCritical": 11,

      "LowerThresholdFatal": 10,

      "MinReadingRange": 0,

      "MaxReadingRange": 20,

      "PhysicalContext": "VoltageRegulator",

      "RelatedItem": [

        {

          "@odata.id": "/redfish/v1/Chassis/1"

        }

      ]

    },

    {

      "@odata.id": "/redfish/v1/Chassis/1/Power#/Voltages/1",

      "MemberId": "1",

      "Name": "VRM2 Voltage",

      "SensorNumber": 12,

      "Status": {

        "State": "Enabled",

        "Health": "OK"

      },

      "ReadingVolts": 5,

      "UpperThresholdNonCritical": 5.5,

      "UpperThresholdCritical": 7,

      "LowerThresholdNonCritical": 4.75,

      "LowerThresholdCritical": 4.5,

      "MinReadingRange": 0,

      "MaxReadingRange": 20,

      "PhysicalContext": "VoltageRegulator",

      "RelatedItem": [

        {

          "@odata.id": "/redfish/v1/Chassis/1"

        }

      ]

    }

  ],

  "PowerSupplies": [

    {

      "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/0",

      "MemberId": "0",

      "Name": "Power Supply Bay 1",

      "Status": {

        "State": "Enabled",

        "Health": "Warning"

      },

      "Oem": {},

      "PowerSupplyType": "DC",

      "LineInputVoltageType": "DCNeg48V",

      "LineInputVoltage": -48,

      "PowerCapacityWatts": 400,

      "LastPowerOutputWatts": 192,

      "Model": "499253-B21",

      "Manufacturer": "ManufacturerName",

      "FirmwareVersion": "1.00",

      "SerialNumber": "1z0000001",

      "PartNumber": "1z0000001A3a",

      "SparePartNumber": "0000001A3a",

      "InputRanges": [

        {

          "InputType": "DC",

          "MinimumVoltage": -47,

          "MaximumVoltage": -49,

          "OutputWattage": 400,

          "Oem": {}

        }

      ],

      "RelatedItem": [

        {

          "@odata.id": "/redfish/v1/Chassis/1"

        }

      ],

      "Redundancy": [

        {

          "@odata.id": "/redfish/v1/Chassis/1/Power#/Redundancy/0"

        }

      ]

    },

    {

      "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/1",

      "MemberId": "1",

      "Name": "Power Supply Bay 2",

      "Status": {

        "State": "Disabled",

        "Health": "Warning"

      },

      "Oem": {},

      "PowerSupplyType": "AC",

      "LineInputVoltageType": "AC240V",

      "LineInputVoltage": 220,

      "PowerCapacityWatts": 400,

      "LastPowerOutputWatts": 190,

      "Model": "499253-B21",

      "Manufacturer": "ManufacturerName",

      "FirmwareVersion": "1.00",

      "SerialNumber": "1z0000001",

      "PartNumber": "1z0000001A3a",

      "SparePartNumber": "0000001A3a",

      "InputRanges": [

        {

          "InputType": "AC",

          "MinimumVoltage": 215,

          "MaximumVoltage": 225,

          "MinimumFrequencyHz": 45,

          "MaximumFrequencyHz": 55,

          "OutputWattage": 400,

          "Oem": {}

        },

        {

          "InputType": "AC",

          "MinimumVoltage": 200,

          "MaximumVoltage": 215,

          "MinimumFrequencyHz": 40,

          "MaximumFrequencyHz": 65,

          "OutputWattage": 380,

          "Oem": {}

        }

      ],

      "RelatedItem": [

        {

          "@odata.id": "/redfish/v1/Chassis/1"

        }

      ],

      "Redundancy": [

        {

          "@odata.id": "/redfish/v1/Chassis/1/Power#/Redundancy/0"

        }

      ]

    }



  ],

  "Redundancy": [

    {

      "@odata.id": "/redfish/v1/Chassis/1/Power#/Redundancy/0",

      "MemberId": "0",

      "Name": "PowerSupply Redundancy Group 1",

      "Mode": "Failover",

      "MaxNumSupported": 2,

      "MinNumNeeded": 1,

      "RedundancySet": [

        {

          "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/0"

        },

        {

          "@odata.id": "/redfish/v1/Chassis/1/Power#/PowerSupplies/1"

        }

      ],

      "Status": {

        "State": "Offline",

        "Health": "OK"

      }

    }

  ],
  "Oem": {}

}