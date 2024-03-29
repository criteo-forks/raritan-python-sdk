# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2022 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "BulkConfiguration.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.bulkcfg

import raritan.rpc.event


# interface
class BulkConfiguration(Interface):
    idlType = "bulkcfg.BulkConfiguration:1.0.2"

    # enumeration
    class Status(Enumeration):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.Status:1.0.0"
        values = ["UNKNOWN", "UPLOAD_FAILED", "RESTORE_PENDING", "RESTORE_OK", "RESTORE_FAILED"]

    Status.UNKNOWN = Status(0)
    Status.UPLOAD_FAILED = Status(1)
    Status.RESTORE_PENDING = Status(2)
    Status.RESTORE_OK = Status(3)
    Status.RESTORE_FAILED = Status(4)

    class _getStatus(Interface.Method):
        name = 'getStatus'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            status = raritan.rpc.bulkcfg.BulkConfiguration.Status.decode(rsp['status'])
            timeStamp = raritan.rpc.Time.decode(rsp['timeStamp'])
            typecheck.is_enum(status, raritan.rpc.bulkcfg.BulkConfiguration.Status, DecodeException)
            typecheck.is_time(timeStamp, DecodeException)
            return (status, timeStamp)

    # enumeration
    class FilterType(Enumeration):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.FilterType:1.0.0"
        values = ["WHITELIST", "BLACKLIST"]

    FilterType.WHITELIST = FilterType(0)
    FilterType.BLACKLIST = FilterType(1)

    # structure
    class Filter(Structure):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.Filter:1.0.0"
        elements = ["name", "displayName", "noOverride", "bulkOnly", "ruleSpecs"]

        def __init__(self, name, displayName, noOverride, bulkOnly, ruleSpecs):
            typecheck.is_string(name, AssertionError)
            typecheck.is_string(displayName, AssertionError)
            typecheck.is_bool(noOverride, AssertionError)
            typecheck.is_bool(bulkOnly, AssertionError)
            for x0 in ruleSpecs:
                typecheck.is_string(x0, AssertionError)

            self.name = name
            self.displayName = displayName
            self.noOverride = noOverride
            self.bulkOnly = bulkOnly
            self.ruleSpecs = ruleSpecs

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                name = json['name'],
                displayName = json['displayName'],
                noOverride = json['noOverride'],
                bulkOnly = json['bulkOnly'],
                ruleSpecs = [x0 for x0 in json['ruleSpecs']],
            )
            return obj

        def encode(self):
            json = {}
            json['name'] = self.name
            json['displayName'] = self.displayName
            json['noOverride'] = self.noOverride
            json['bulkOnly'] = self.bulkOnly
            json['ruleSpecs'] = [x0 for x0 in self.ruleSpecs]
            return json

    # structure
    class FilterProfile(Structure):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.FilterProfile:1.0.0"
        elements = ["name", "description", "filterNameToTypeMap"]

        def __init__(self, name, description, filterNameToTypeMap):
            typecheck.is_string(name, AssertionError)
            typecheck.is_string(description, AssertionError)

            self.name = name
            self.description = description
            self.filterNameToTypeMap = filterNameToTypeMap

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                name = json['name'],
                description = json['description'],
                filterNameToTypeMap = dict([(
                    elem['key'],
                    raritan.rpc.bulkcfg.BulkConfiguration.FilterType.decode(elem['value']))
                    for elem in json['filterNameToTypeMap']]),
            )
            return obj

        def encode(self):
            json = {}
            json['name'] = self.name
            json['description'] = self.description
            json['filterNameToTypeMap'] = [dict(
                key = k,
                value = raritan.rpc.bulkcfg.BulkConfiguration.FilterType.encode(v))
                for k, v in self.filterNameToTypeMap.items()]
            return json

    # structure
    class Settings(Structure):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.Settings:1.0.0"
        elements = ["filterProfiles", "defaultProfileName"]

        def __init__(self, filterProfiles, defaultProfileName):
            for x0 in filterProfiles:
                typecheck.is_struct(x0, raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile, AssertionError)
            typecheck.is_string(defaultProfileName, AssertionError)

            self.filterProfiles = filterProfiles
            self.defaultProfileName = defaultProfileName

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                filterProfiles = [raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile.decode(x0, agent) for x0 in json['filterProfiles']],
                defaultProfileName = json['defaultProfileName'],
            )
            return obj

        def encode(self):
            json = {}
            json['filterProfiles'] = [raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile.encode(x0) for x0 in self.filterProfiles]
            json['defaultProfileName'] = self.defaultProfileName
            return json

    # value object
    class SettingsChangedEvent(raritan.rpc.event.UserEvent):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.SettingsChangedEvent:1.0.0"

        def __init__(self, actUserName, actIpAddr, source):
            super(raritan.rpc.bulkcfg.BulkConfiguration.SettingsChangedEvent, self).__init__(actUserName, actIpAddr, source)

        def encode(self):
            json = super(raritan.rpc.bulkcfg.BulkConfiguration.SettingsChangedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.bulkcfg.BulkConfiguration.SettingsChangedEvent, self).listElements()
            return elements

    # value object
    class SavedEvent(raritan.rpc.event.UserEvent):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.SavedEvent:1.0.0"

        def __init__(self, isBackup, actUserName, actIpAddr, source):
            super(raritan.rpc.bulkcfg.BulkConfiguration.SavedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_bool(isBackup, AssertionError)

            self.isBackup = isBackup

        def encode(self):
            json = super(raritan.rpc.bulkcfg.BulkConfiguration.SavedEvent, self).encode()
            json['isBackup'] = self.isBackup
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                isBackup = json['isBackup'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["isBackup"]
            elements = elements + super(raritan.rpc.bulkcfg.BulkConfiguration.SavedEvent, self).listElements()
            return elements

    # value object
    class RestoredEvent(raritan.rpc.event.UserEvent):
        idlType = "bulkcfg.BulkConfiguration_1_0_2.RestoredEvent:1.0.0"

        def __init__(self, isBackup, actUserName, actIpAddr, source):
            super(raritan.rpc.bulkcfg.BulkConfiguration.RestoredEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_bool(isBackup, AssertionError)

            self.isBackup = isBackup

        def encode(self):
            json = super(raritan.rpc.bulkcfg.BulkConfiguration.RestoredEvent, self).encode()
            json['isBackup'] = self.isBackup
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                isBackup = json['isBackup'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["isBackup"]
            elements = elements + super(raritan.rpc.bulkcfg.BulkConfiguration.RestoredEvent, self).listElements()
            return elements

    SUCCESS = 0

    ERR_FILTER_NAME_UNKNOWN = 1

    ERR_FILTER_TYPE_READONLY = 2

    ERR_PROFILE_ALREADY_EXISTS = 3

    ERR_PROFILE_DOES_NOT_EXIST = 4

    ERR_PROFILE_IS_DEFAULT = 5

    ERR_PROFILE_IS_BUILTIN = 6

    ERR_PROFILE_NAME_TOO_LONG = 7

    ERR_PROFILE_NAME_INVALID = 8

    ERR_PROFILE_TOO_MANY = 9

    class _getFilters(Interface.Method):
        name = 'getFilters'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [raritan.rpc.bulkcfg.BulkConfiguration.Filter.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_struct(x0, raritan.rpc.bulkcfg.BulkConfiguration.Filter, DecodeException)
            return _ret_

    class _getFilterProfiles(Interface.Method):
        name = 'getFilterProfiles'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_struct(x0, raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile, DecodeException)
            return _ret_

    class _addFilterProfile(Interface.Method):
        name = 'addFilterProfile'

        @staticmethod
        def encode(profile):
            typecheck.is_struct(profile, raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile, AssertionError)
            args = {}
            args['profile'] = raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile.encode(profile)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _modifyFilterProfile(Interface.Method):
        name = 'modifyFilterProfile'

        @staticmethod
        def encode(profile):
            typecheck.is_struct(profile, raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile, AssertionError)
            args = {}
            args['profile'] = raritan.rpc.bulkcfg.BulkConfiguration.FilterProfile.encode(profile)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _deleteFilterProfile(Interface.Method):
        name = 'deleteFilterProfile'

        @staticmethod
        def encode(profileName):
            typecheck.is_string(profileName, AssertionError)
            args = {}
            args['profileName'] = profileName
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getDefaultFilterProfileName(Interface.Method):
        name = 'getDefaultFilterProfileName'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_string(_ret_, DecodeException)
            return _ret_

    class _selectDefaultFilterProfile(Interface.Method):
        name = 'selectDefaultFilterProfile'

        @staticmethod
        def encode(profileName):
            typecheck.is_string(profileName, AssertionError)
            args = {}
            args['profileName'] = profileName
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.bulkcfg.BulkConfiguration.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.bulkcfg.BulkConfiguration.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.bulkcfg.BulkConfiguration.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.bulkcfg.BulkConfiguration.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(BulkConfiguration, self).__init__(target, agent)
        self.getStatus = BulkConfiguration._getStatus(self)
        self.getFilters = BulkConfiguration._getFilters(self)
        self.getFilterProfiles = BulkConfiguration._getFilterProfiles(self)
        self.addFilterProfile = BulkConfiguration._addFilterProfile(self)
        self.modifyFilterProfile = BulkConfiguration._modifyFilterProfile(self)
        self.deleteFilterProfile = BulkConfiguration._deleteFilterProfile(self)
        self.getDefaultFilterProfileName = BulkConfiguration._getDefaultFilterProfileName(self)
        self.selectDefaultFilterProfile = BulkConfiguration._selectDefaultFilterProfile(self)
        self.getSettings = BulkConfiguration._getSettings(self)
        self.setSettings = BulkConfiguration._setSettings(self)

# from raritan/rpc/bulkcfg/__extend__.py
try:
    # Python 3
    from urllib.parse import quote
except ImportError:
    # Python 2
    from urllib2 import quote

def upload(agent, data, backup = False, password = None, skip_check = "", link_ids = []):
    """
    Method to upload bulk config files.
    Check the according response header X-Response-Code for succesfull configuration.

    **parameters**, **return**

    :param agent: An agent instance for the device where the config should be uploaded
    :param data: The binary data of the bulk config file
    :param backup: (optional) Is the file a backup?
    :param password: (optional) The password for the config file
    :param skip_check: (optional) Skip check for model/firmware version. Values: "model", "firmware_version", "firmware_version,model"
    :param link_ids: (optional) A List of linked device ids e.g. link_ids=[1,2]
    :return: return the response code from internal processing

    **Example**
        :Example:

        from raritan import rpc
        from raritan.rpc import bulkcfg

        agent = rpc.Agent("https", "my-pdu.example.com", "admin", "raritan")

        # read file in binary mode
        cfgFile = open("bulk_config.txt", "rb")
        # upload
        code = bulkcfg.upload(agent, cfgFile.read())
        # view code
        print(code)
    """
    target = "cgi-bin/bulk_config_restore.cgi"
    params = []
    if password:
        params.append("user_password=" + quote(password))
    if skip_check:
        params.append("skip_checks=" + skip_check)
    if link_ids:
        params.append("link_ids=" + ",".join(str(x) for x in link_ids))
    else:
        params.append("link_ids=1") #default to 1 as master
    if backup:
        params.append("mode=backup")
    if params:
        target += "?%s" % "&".join(params)
    formdata = [dict(data=data, filename="bulk_config.txt", formname="bulk_config_file", mimetype="application/octet-stream")]
    response = agent.form_data_file(target, formdata)
    return int(response["headers"].get("X-Response-Code"))

def download(agent, backup = False, password = None, clear_text = False, link_ids = [], filter_profile = ""):
    """
    Method to download the bulk config file

    **parameters**

    :param agent: An agent instance from the device where the bulk config should be downloaded
    :param backup: (optional) Download a backup?
    :param password: (optional) A password for encrypting the config file
    :param clear_text: (optional) Get config as cleartext. Overrides password parameter
    :param link_ids: (optional) A List of linked device ids e.g. link_ids=[1,2]
    :param filter_profile: (optional) The profile to download as name e.g. filter_profile="http_settings"
    :return: returns the bulk configuration data

    **Example**
        :Example:

        from raritan import rpc
        from raritan.rpc import bulkcfg

        agent = rpc.Agent("https", "my-pdu.example.com", "admin", "raritan")
        # download
        cfg = bulkcfg.download(agent)
        print(cfg)
    """
    target = "cgi-bin/bulk_config_save.cgi"
    params = []
    if password:
        params.append("bulk_config_password=" + quote(password))
    if clear_text:
        params.append("config_format=cleartext")
    if link_ids:
        params.append("link_ids=" + ",".join(str(x) for x in link_ids))
    else:
        params.append("link_ids=1") #default to 1 as master
    if filter_profile:
        params.append("filter_profile=" + quote(str(filter_profile)))
    if backup:
        params.append("mode=backup")
    if params:
        target += "?%s" % "&".join(params)
    return agent.get(target)
