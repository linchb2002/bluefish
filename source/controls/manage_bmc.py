#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime
import obmc_dbuslib
from manage_network import *
from manage_fwversion import *


def set_bmc_warm_reset(action):
    result = {}
    if action.upper() == 'WARMRESET':
        op = 'WarmReset'
    else:
        return set_failure_dict("Unknown parameter", completion_code.failure)
    try:
        dbusctl = obmc_dbuslib.ObmcRedfishProviders()
        dbusctl.bmc_reset_operation(str(op))
    except Exception, e:
        return set_failure_dict(('Exception:', e), completion_code.failure)

    return set_success_dict(result)


def set_bmc_fwupdate(action):
    result = {}
    if action.upper() == 'PREPARE':
        op = 'Prepare'
    elif action.upper() == 'APPLY':
        op = 'Apply'
    elif action.upper() == 'ABORT':
        op = 'Abort'
    else:
        return set_failure_dict("Unknown parameter", completion_code.failure)
    try:
        dbusctl = obmc_dbuslib.ObmcRedfishProviders()
        dbusctl.fw_update_operation(str(op))
    except Exception, e:
        return set_failure_dict(('Exception:', e), completion_code.failure)

    return set_success_dict(result)


def get_bmc_fwupdate_state(action):
    result = {}

    if action.upper() == 'QUERY':
        op = 'Query'
        try:
            dbusctl = obmc_dbuslib.ObmcRedfishProviders()
            pydata = dbusctl.fw_update_operation(str(op))
            newdata = pydata.replace('\n', '  ')
        except Exception, e:
            return set_failure_dict(('Exception:', e), completion_code.failure)
    else:
        return set_failure_dict("Unknown parameter", completion_code.failure)
    result["UPDATE_PROGRESS"] = newdata
    result[completion_code.cc_key] = completion_code.success
    return result


def set_bmc_attention_led(setting):
    result = {}
    try:
        dbusctl = obmc_dbuslib.ObmcRedfishProviders()
        dbusctl.led_operation(str(setting), 'identify')
    
    except Exception,e:
        return set_failure_dict(('Exception:', e),completion_code.failure)

    return set_success_dict(result)


def get_bmc_attention_led_status():
    result = {}

    try:
        dbusctl = obmc_dbuslib.ObmcRedfishProviders()
        pydata = dbusctl.led_operation('state', 'identify')

    except Exception,e:
        return set_failure_dict(('Exception:', e),completion_code.failure)
    
    if(pydata == 'Off'):
        result["Chassis_IndicatorLED"] = 'Off'
    elif (pydata == 'Lit'):
        result["Chassis_IndicatorLED"] = 'Lit'
    elif (pydata == 'Blinking'):
        result["Chassis_IndicatorLED"] = 'Blinking'
    else:
        result["Chassis_IndicatorLED"] = 'Unknown'
                
    return set_success_dict(result)


def show_bmc_hostname():
    result = {}

    result["Hostname"] = socket.gethostname()
    result[completion_code.cc_key] = completion_code.success

    return result




def get_bmc_time():
    """ Returns current date and time in UTC
    """
    try:
        result = {}

        now = str(datetime.datetime.utcnow())

        result["Year"] = now[0:4]
        result["Month"] = now[5:7]
        result["Day"] = now[8:10]
        result["Hour"] = now[11:13]
        result["Min"] = now[14:16]
        result["Sec"] = now[17:19]

        return set_success_dict(result)

    except Exception, e:
        return set_failure_dict("get_bmc_time() Exception: {0}".format(e))


def show_bmc_time(edm=False):
    """ Returns formatted date and time in UTC
    """
    try:
        result = {}

        now = get_bmc_time()

        if edm:
            result["DateTime"] = "{0}-{1}-{2}T{3}:{4}:{5}Z".format(now["Year"], now["Month"], now["Day"],
                                                                   now["Hour"], now["Min"], now["Sec"])
        else:
            result["DateTime"] = "{0}-{1}-{2} {3}:{4}:{5}".format(now["Year"], now["Month"], now["Day"],
                                                                  now["Hour"], now["Min"], now["Sec"])

        return set_success_dict(result)

    except Exception, e:
        return set_failure_dict("show_rack_manager_time() Exception: {0}".format(e))


def set_bmc_time(datetime=None, hour=-1, min=-1, sec=-1, month=-1, day=-1, year=-1):
    """ Sets system date and time
    """
    try:
        if datetime is not None:
            year, month, day, hour, min, sec = re.findall("\\d+", datetime)
        else:
            now = get_bmc_time()

            if hour == -1:
                hour = now["Hour"]
            elif hour > 23 or hour < 0:
                return set_failure_dict("Hour value out of range (0-23): {0}".format(hour), completion_code.failure)
            if min == -1:
                min = now["Min"]
            elif min > 59 or min < 0:
                return set_failure_dict("Minute value out of range (0-59): {0}".format(min), completion_code.failure)
            if sec == -1:
                sec = now["Sec"]
            elif sec > 59 or sec < 0:
                return set_failure_dict("Second value out of range (0-59): {0}".format(sec), completion_code.failure)
            if month == -1:
                month = now["Month"]
            elif month > 12 or month < 1:
                return set_failure_dict("Month value out of range (1-12): {0}".format(month), completion_code.failure)
            if day == -1:
                day = now["Day"]
            elif day > 31 or day < 1:
                return set_failure_dict("Day value out of range (1-31): {0}".format(day), completion_code.failure)
            if year == -1:
                year = now["Year"]

        newdate = "{0}-{1}-{2} {3}:{4}:{5}".format(year, month, day, hour, min, sec)

        pipe = subprocess.check_output(["date", "-s", newdate], stderr=subprocess.STDOUT)

        return set_success_dict()

    except subprocess.CalledProcessError as e:
        return set_failure_dict("Failed to set system time: {0}".format(e.output.strip()), completion_code.failure)

    except Exception, e:
        return set_failure_dict("set_rack_manager_time() Exception: {0}".format(e))
