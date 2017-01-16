import os
import get_handler
import patch_handler
import post_handler
import delete_handler
from pre_settings import rm_mode_enum
from authentication import get_op_mode

TEMPLATE_ROOT = os.path.realpath ("/usr/lib/redfish/templates") + "/"

class redfish_resource:
    """
    Defines a single resource accessible via the REST interface.
    """
    
    def __init__ (self, common = None, pmdu = None, row = None, stand_alone = None,
        get = None, post = None, patch = None, delete = None):
        """
        Initialize a resource to be provided by the REST interface.  The resource is initialized
        with the URI and template path for each configuration and the methods that are supported
        by the resource.
        
        :param common: A tuple of URI and template path for a resource that is common to all
        configurations.  If not specified, the specific configuration settings will be applied.
        :param pmdu: A tuple of URI and template path for the resource when configured as a rack
        manager with a PMDU.  If not specified, the resource will not be available in the PMDU rack
        manager configuration unless the information is provided as a common resource.
        :param row: A tuple of URI and template path for the resource when configured as a row
        manager.  If not specified, the resource will not be available in the row manager
        configuration unless the information is provided as a common resource.
        :param stand_alone: A tuple of URI and template path for the resource when configured as a
        stand-alone rack manager.  If not specified, the resource will not be available in the
        stand-alone rack manager configuration unless the information is provided as a common
        resource.
        :param get: The handler for GET requests for the resource.  If not specified, GET requests
        on the resource will not be supported.
        :param post: The handler for POST requests for the resource.  If not specified, POST
        requests on the resource will not be supported.
        :param patch: The handler for PATCH requests for the resource.  If not specified, PATCH
        requests on the resource will not be supported.
        :param delete: The handler for DELETE requests for the resource.  If not specified, DELETE
        requests on the resource will not be supported.
        """
        
        self.common = common
        self.pmdu = pmdu
        self.row = row
        self.stand_alone = stand_alone
        self.get = get
        self.post = post
        self.patch = patch
        self.delete = delete
        
    def register_resource (self, app, mode):
        """
        Register the resource with the REST handler.  If the resource is not valid for the given
        configuration, this call does nothing.
        
        :param app: The web server instance to register the resource with.
        :param mode: The manager configuration that should be registered.
        """
        
        if (self.common):
            self.rest = self.common[0]
            self.template = TEMPLATE_ROOT + self.common[1]
        elif (self.pmdu and ((mode == rm_mode_enum.pmdu_rackmanager) or
            (mode == rm_mode_enum.tfb_dev_benchtop) or (mode == rm_mode_enum.unknown_rm_mode))):
            self.rest = self.pmdu[0]
            self.template = TEMPLATE_ROOT + self.pmdu[1]
        elif (self.row and (mode == rm_mode_enum.rowmanager)):
            self.rest = self.row[0]
            self.template = TEMPLATE_ROOT + self.row[1]
        elif (self.stand_alone and (mode == rm_mode_enum.standalone_rackmanager)):
            self.rest = self.stand_alone[0]
            self.template = TEMPLATE_ROOT + self.stand_alone[1]
        else:
            self.rest = None
            
        if (not self.rest):
            return
        (self.path, self.file) = os.path.split (self.template)
        
        if (self.get):
            app.route (self.rest, "GET", self.get)
        if (self.post):
            app.route (self.rest, "POST", self.post)
        if (self.patch):
            app.route (self.rest, "PATCH", self.patch)
        if (self.delete):
            app.route (self.rest, "DELETE", self.delete)

def get_max_num_systems ():
    """
    Get the maximum number of possible systems for the current configuration.
    
    :return The maximum number of systems.
    """
    
    return 24 if (get_op_mode () == rm_mode_enum.standalone_rackmanager) else 48

REGEX_1_48 = "[1-3][0-9]|4[0-8]|[1-9]"
REGEX_1_24 = "1[0-9]|2[0-4]|[1-9]"

def id_filter (config):
    """
    A bottle router filter that matches valid identifier numbers.  Based on the config, it will
    match against 24 or 48 valid IDs.
    
    :param config: The number of IDs to filter against.  This defaults to 48 if not sepeified or if
    the range isn't supported.
    """
    
    valid = config or 48
    regex = REGEX_1_24 if (int (valid) == 24) else REGEX_1_48
    
    def to_python (match):
        return match
    
    def to_url (system):
        return system
    
    return regex, to_python, to_url

def system_id_filter (config):
    """
    A Bottle router filter that matches a system identifier against valid values.
    """
    
    return id_filter (get_max_num_systems ())

def add_bottle_filters (app):
    """
    Add custom URL filters to the Bottle instance.
    
    :param app: The web server instance to add the filters to.
    """
    
    app.router.add_filter ("id", id_filter)
    app.router.add_filter ("sysid", system_id_filter)

##
# The list of accesible resources from the REST interface.
##
REDFISH_RESOURCES = {
    ###################
    # Top-Level Redfish
    ###################
    "version" : redfish_resource (
        common = (
            "/redfish",
            "Redfish.tpl"),
        get = get_handler.get_redfish_version),
    "service_root" : redfish_resource (
        common = (
            "/redfish/v1",
            "ServiceRoot.tpl"),
        get = get_handler.get_service_root),
    "chassis_root" : redfish_resource (
        common = (
            "/redfish/v1/Chassis",
            "Chassis.tpl"),
        get = get_handler.get_chassis_root),
    "managers_root" : redfish_resource (
        common = (
            "/redfish/v1/Managers",
            "Managers.tpl"),
        get = get_handler.get_managers_root),
 
   
    #########################
    # Chassis components
    #########################      
    "chassis" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/1",
        "Chassis/Chassis.tpl"),
        get = get_handler.get_chassis),
   "chassis_temperature" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/1/Thermal",
        "Chassis/Temperature.tpl"),
        get = get_handler.get_chassis_temperature),  #ToDo#
   "chassis_redundancy" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/1/Thermal#/Redundancy/0",
        "Chassis/Redundancy.tpl"),
        get = get_handler.get_chassis_redundancy),  #ToDo#
    "chassis_power" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/1/Power",
        "Chassis/Power.tpl"),
        get = get_handler.get_chassis_power),  #ToDo#
    "chassis_power_redundancy" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/1/Power#/Redundancy/0",
        "Chassis/PowerRedundancy.tpl"),
        get = get_handler.get_chassis_power_redundancy),  #ToDo#   
    "chassis_enc1" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/Enc1",
        "Chassis/Enc1.tpl"),
        get = get_handler.get_chassis_enc1),  #ToDo#   
    "chassis_storage_enclosure" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/StorageEnclosure<se_id>",
        "Chassis/StorageEnclosure.tpl"),
        get = get_handler.get_chassis_storage_enclosure),  #ToDo# 
        
    "chassis_storage_enclosure_disk" : redfish_resource (
        common = (
        "/redfish/v1/Chassis/StorageEnclosure<se_id>/Drives/Disk.Bay<disk_id>",
        "Chassis/Disk.tpl"),
        get = get_handler.get_chassis_storage_enclosure_disk,  #ToDo#  
        post = post_handler.post_chassis_storage_enclosure_disk), #ToDo#  

    
    #########################
    # BMC components
    #########################   
    "bmc" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1",
        "BMC/BMC.tpl"),
        get = get_handler.get_bmc,  #ToDo#
        patch = patch_handler.patch_bmc),  #ToDo#
    "bmc_networkprotocol" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/NetworkProtocol",
        "BMC/NetworkProtocol.tpl"),
        get = get_handler.get_bmc_networkprotocol),   #ToDo#
    "bmc_ethernets" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/EthernetInterfaces",
        "BMC/EthernetInterfaces.tpl"),
        get = get_handler.get_bmc_ethernets),
    "bmc_ethernet" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/EthernetInterface/<eth:re:eth[0|1]>",
        "BMC/EthernetInterface.tpl"),
        get = get_handler.get_bmc_ethernet,
        patch = patch_handler.patch_bmc_ethernet),
    "bmc_log_service" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/LogServices",
        "BMC/LogServices.tpl"),
        get = get_handler.get_bmc_log_services),
    "bmc_log" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/LogServices/Log",
        "BMC/Log.tpl"),
        get = get_handler.get_bmc_log),
    "bmc_clear_log" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/LogServices/Log/Actions/LogService.ClearLog",
        "GeneralError.tpl"),
        post = post_handler.post_bmc_clear_log),
        
    "bmc_log_entries" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/LogServices/Log/Entries",
        "BMC/LogEntries.tpl"),
        get = get_handler.get_bmc_log_entries),
    "bmc_log_entry" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/LogServices/Log/Entry/<entry>",
        "BMC/LogEntry.tpl"),
        get = get_handler.get_bmc_log_entry),    
    "bmc_serialinterfaces" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/SerialInterfaces",
        "BMC/SerialInterfaces.tpl"),
        get = get_handler.get_bmc_serialinterfaces),    #ToDo#
    "bmc_serialinterface" : redfish_resource (
        common = (
        "/redfish/v1/Managers/1/SerialInterface",
        "BMC/SerialInterface.tpl"),
        get = get_handler.get_bmc_serialinterface),    #ToDo#
        

 
    ############################
    # Account service components
    ############################
    "account_service" : redfish_resource (
        common = (
            "/redfish/v1/AccountService",
            "AccountService/AccountService.tpl"),
        get = get_handler.get_account_service),
    "accounts" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/ManagerAccounts",
            "AccountService/ManagerAccounts.tpl"),
        get = get_handler.get_accounts,
        post = post_handler.post_accounts),
    "account" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/ManagerAccount/<account>",
            "AccountService/ManagerAccount.tpl"),
        get = get_handler.get_account,
        patch = patch_handler.patch_account,
        delete = delete_handler.delete_account),
    "roles" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/Roles",
            "AccountService/Roles.tpl"),
        get = get_handler.get_roles),
    "admin" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/Role/admin",
            "AccountService/ocs_admin.tpl"),
        get = get_handler.get_ocs_admin),
    "operator" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/Role/operator",
            "AccountService/ocs_operator.tpl"),
        get = get_handler.get_ocs_operator),
    "user" : redfish_resource (
        common = (
            "/redfish/v1/AccountService/Role/user",
            "AccountService/ocs_user.tpl"),
        get = get_handler.get_ocs_user),
    

}
