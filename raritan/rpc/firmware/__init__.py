# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2022 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "Firmware.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.firmware

import raritan.rpc.idl


# enumeration
class UpdateHistoryStatus(Enumeration):
    idlType = "firmware.UpdateHistoryStatus:1.0.0"
    values = ["SUCCESSFUL", "FAILED", "INCOMPLETE"]

UpdateHistoryStatus.SUCCESSFUL = UpdateHistoryStatus(0)
UpdateHistoryStatus.FAILED = UpdateHistoryStatus(1)
UpdateHistoryStatus.INCOMPLETE = UpdateHistoryStatus(2)

# structure
class UpdateHistoryEntry(Structure):
    idlType = "firmware.UpdateHistoryEntry:1.0.0"
    elements = ["timestamp", "oldVersion", "imageVersion", "imageMD5", "status"]

    def __init__(self, timestamp, oldVersion, imageVersion, imageMD5, status):
        typecheck.is_time(timestamp, AssertionError)
        typecheck.is_string(oldVersion, AssertionError)
        typecheck.is_string(imageVersion, AssertionError)
        typecheck.is_string(imageMD5, AssertionError)
        typecheck.is_enum(status, raritan.rpc.firmware.UpdateHistoryStatus, AssertionError)

        self.timestamp = timestamp
        self.oldVersion = oldVersion
        self.imageVersion = imageVersion
        self.imageMD5 = imageMD5
        self.status = status

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            timestamp = raritan.rpc.Time.decode(json['timestamp']),
            oldVersion = json['oldVersion'],
            imageVersion = json['imageVersion'],
            imageMD5 = json['imageMD5'],
            status = raritan.rpc.firmware.UpdateHistoryStatus.decode(json['status']),
        )
        return obj

    def encode(self):
        json = {}
        json['timestamp'] = raritan.rpc.Time.encode(self.timestamp)
        json['oldVersion'] = self.oldVersion
        json['imageVersion'] = self.imageVersion
        json['imageMD5'] = self.imageMD5
        json['status'] = raritan.rpc.firmware.UpdateHistoryStatus.encode(self.status)
        return json

# enumeration
class ImageState(Enumeration):
    idlType = "firmware.ImageState:1.0.0"
    values = ["NONE", "UPLOADING", "UPLOAD_FAILED", "DOWNLOADING", "DOWNLOAD_FAILED", "COMPLETE"]

ImageState.NONE = ImageState(0)
ImageState.UPLOADING = ImageState(1)
ImageState.UPLOAD_FAILED = ImageState(2)
ImageState.DOWNLOADING = ImageState(3)
ImageState.DOWNLOAD_FAILED = ImageState(4)
ImageState.COMPLETE = ImageState(5)

# structure
class ImageStatus(Structure):
    idlType = "firmware.ImageStatus:1.0.0"
    elements = ["state", "error_message", "time_started", "size_total", "size_done"]

    def __init__(self, state, error_message, time_started, size_total, size_done):
        typecheck.is_enum(state, raritan.rpc.firmware.ImageState, AssertionError)
        typecheck.is_string(error_message, AssertionError)
        typecheck.is_time(time_started, AssertionError)
        typecheck.is_int(size_total, AssertionError)
        typecheck.is_int(size_done, AssertionError)

        self.state = state
        self.error_message = error_message
        self.time_started = time_started
        self.size_total = size_total
        self.size_done = size_done

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            state = raritan.rpc.firmware.ImageState.decode(json['state']),
            error_message = json['error_message'],
            time_started = raritan.rpc.Time.decode(json['time_started']),
            size_total = json['size_total'],
            size_done = json['size_done'],
        )
        return obj

    def encode(self):
        json = {}
        json['state'] = raritan.rpc.firmware.ImageState.encode(self.state)
        json['error_message'] = self.error_message
        json['time_started'] = raritan.rpc.Time.encode(self.time_started)
        json['size_total'] = self.size_total
        json['size_done'] = self.size_done
        return json

# structure
class ImageInfo(Structure):
    idlType = "firmware.ImageInfo:1.0.1"
    elements = ["valid", "version", "min_required_version", "min_downgrade_version", "product", "platform", "oem", "hwid_whitelist", "hwid_blacklist", "compatible", "signature_present", "signed_by", "signature_good", "certified_by", "certificate_good", "model_list_present", "model_supported"]

    def __init__(self, valid, version, min_required_version, min_downgrade_version, product, platform, oem, hwid_whitelist, hwid_blacklist, compatible, signature_present, signed_by, signature_good, certified_by, certificate_good, model_list_present, model_supported):
        typecheck.is_bool(valid, AssertionError)
        typecheck.is_string(version, AssertionError)
        typecheck.is_string(min_required_version, AssertionError)
        typecheck.is_string(min_downgrade_version, AssertionError)
        typecheck.is_string(product, AssertionError)
        typecheck.is_string(platform, AssertionError)
        typecheck.is_string(oem, AssertionError)
        typecheck.is_string(hwid_whitelist, AssertionError)
        typecheck.is_string(hwid_blacklist, AssertionError)
        typecheck.is_bool(compatible, AssertionError)
        typecheck.is_bool(signature_present, AssertionError)
        typecheck.is_string(signed_by, AssertionError)
        typecheck.is_bool(signature_good, AssertionError)
        typecheck.is_string(certified_by, AssertionError)
        typecheck.is_bool(certificate_good, AssertionError)
        typecheck.is_bool(model_list_present, AssertionError)
        typecheck.is_bool(model_supported, AssertionError)

        self.valid = valid
        self.version = version
        self.min_required_version = min_required_version
        self.min_downgrade_version = min_downgrade_version
        self.product = product
        self.platform = platform
        self.oem = oem
        self.hwid_whitelist = hwid_whitelist
        self.hwid_blacklist = hwid_blacklist
        self.compatible = compatible
        self.signature_present = signature_present
        self.signed_by = signed_by
        self.signature_good = signature_good
        self.certified_by = certified_by
        self.certificate_good = certificate_good
        self.model_list_present = model_list_present
        self.model_supported = model_supported

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            valid = json['valid'],
            version = json['version'],
            min_required_version = json['min_required_version'],
            min_downgrade_version = json['min_downgrade_version'],
            product = json['product'],
            platform = json['platform'],
            oem = json['oem'],
            hwid_whitelist = json['hwid_whitelist'],
            hwid_blacklist = json['hwid_blacklist'],
            compatible = json['compatible'],
            signature_present = json['signature_present'],
            signed_by = json['signed_by'],
            signature_good = json['signature_good'],
            certified_by = json['certified_by'],
            certificate_good = json['certificate_good'],
            model_list_present = json['model_list_present'],
            model_supported = json['model_supported'],
        )
        return obj

    def encode(self):
        json = {}
        json['valid'] = self.valid
        json['version'] = self.version
        json['min_required_version'] = self.min_required_version
        json['min_downgrade_version'] = self.min_downgrade_version
        json['product'] = self.product
        json['platform'] = self.platform
        json['oem'] = self.oem
        json['hwid_whitelist'] = self.hwid_whitelist
        json['hwid_blacklist'] = self.hwid_blacklist
        json['compatible'] = self.compatible
        json['signature_present'] = self.signature_present
        json['signed_by'] = self.signed_by
        json['signature_good'] = self.signature_good
        json['certified_by'] = self.certified_by
        json['certificate_good'] = self.certificate_good
        json['model_list_present'] = self.model_list_present
        json['model_supported'] = self.model_supported
        return json

# enumeration
class UpdateFlags(Enumeration):
    idlType = "firmware.UpdateFlags:1.0.0"
    values = ["CROSS_OEM", "CROSS_HW", "ALLOW_UNTRUSTED"]

UpdateFlags.CROSS_OEM = UpdateFlags(0)
UpdateFlags.CROSS_HW = UpdateFlags(1)
UpdateFlags.ALLOW_UNTRUSTED = UpdateFlags(2)

# value object
class SystemStartupEvent(raritan.rpc.idl.Event):
    idlType = "firmware.SystemStartupEvent:1.0.0"

    def __init__(self, source):
        super(raritan.rpc.firmware.SystemStartupEvent, self).__init__(source)

    def encode(self):
        json = super(raritan.rpc.firmware.SystemStartupEvent, self).encode()
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = []
        elements = elements + super(raritan.rpc.firmware.SystemStartupEvent, self).listElements()
        return elements

# value object
class SystemShutdownEvent(raritan.rpc.event.UserEvent):
    idlType = "firmware.SystemShutdownEvent:1.0.0"

    def __init__(self, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.SystemShutdownEvent, self).__init__(actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.firmware.SystemShutdownEvent, self).encode()
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
        elements = elements + super(raritan.rpc.firmware.SystemShutdownEvent, self).listElements()
        return elements

# value object
class FirmwareValidationFailedEvent(raritan.rpc.event.UserEvent):
    idlType = "firmware.FirmwareValidationFailedEvent:1.0.0"

    def __init__(self, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.FirmwareValidationFailedEvent, self).__init__(actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.firmware.FirmwareValidationFailedEvent, self).encode()
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
        elements = elements + super(raritan.rpc.firmware.FirmwareValidationFailedEvent, self).listElements()
        return elements

# value object
class FirmwareUpdateEvent(raritan.rpc.event.UserEvent):
    idlType = "firmware.FirmwareUpdateEvent:1.0.0"

    def __init__(self, oldVersion, newVersion, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.FirmwareUpdateEvent, self).__init__(actUserName, actIpAddr, source)
        typecheck.is_string(oldVersion, AssertionError)
        typecheck.is_string(newVersion, AssertionError)

        self.oldVersion = oldVersion
        self.newVersion = newVersion

    def encode(self):
        json = super(raritan.rpc.firmware.FirmwareUpdateEvent, self).encode()
        json['oldVersion'] = self.oldVersion
        json['newVersion'] = self.newVersion
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            oldVersion = json['oldVersion'],
            newVersion = json['newVersion'],
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = ["oldVersion", "newVersion"]
        elements = elements + super(raritan.rpc.firmware.FirmwareUpdateEvent, self).listElements()
        return elements

# value object
class FirmwareUpdateStartedEvent(FirmwareUpdateEvent):
    idlType = "firmware.FirmwareUpdateStartedEvent:1.0.0"

    def __init__(self, oldVersion, newVersion, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.FirmwareUpdateStartedEvent, self).__init__(oldVersion, newVersion, actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.firmware.FirmwareUpdateStartedEvent, self).encode()
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            # for firmware.FirmwareUpdateEvent
            oldVersion = json['oldVersion'],
            newVersion = json['newVersion'],
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = []
        elements = elements + super(raritan.rpc.firmware.FirmwareUpdateStartedEvent, self).listElements()
        return elements

# value object
class FirmwareUpdateCompletedEvent(FirmwareUpdateEvent):
    idlType = "firmware.FirmwareUpdateCompletedEvent:1.0.0"

    def __init__(self, oldVersion, newVersion, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.FirmwareUpdateCompletedEvent, self).__init__(oldVersion, newVersion, actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.firmware.FirmwareUpdateCompletedEvent, self).encode()
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            # for firmware.FirmwareUpdateEvent
            oldVersion = json['oldVersion'],
            newVersion = json['newVersion'],
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = []
        elements = elements + super(raritan.rpc.firmware.FirmwareUpdateCompletedEvent, self).listElements()
        return elements

# value object
class FirmwareUpdateFailedEvent(FirmwareUpdateEvent):
    idlType = "firmware.FirmwareUpdateFailedEvent:1.0.0"

    def __init__(self, oldVersion, newVersion, actUserName, actIpAddr, source):
        super(raritan.rpc.firmware.FirmwareUpdateFailedEvent, self).__init__(oldVersion, newVersion, actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.firmware.FirmwareUpdateFailedEvent, self).encode()
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            # for firmware.FirmwareUpdateEvent
            oldVersion = json['oldVersion'],
            newVersion = json['newVersion'],
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = []
        elements = elements + super(raritan.rpc.firmware.FirmwareUpdateFailedEvent, self).listElements()
        return elements

# interface
class Firmware(Interface):
    idlType = "firmware.Firmware:2.0.2"

    class _reboot(Interface.Method):
        name = 'reboot'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _factoryReset(Interface.Method):
        name = 'factoryReset'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _hardFactoryReset(Interface.Method):
        name = 'hardFactoryReset'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _manufacturingReset(Interface.Method):
        name = 'manufacturingReset'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getVersion(Interface.Method):
        name = 'getVersion'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_string(_ret_, DecodeException)
            return _ret_

    class _getUpdateHistory(Interface.Method):
        name = 'getUpdateHistory'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [raritan.rpc.firmware.UpdateHistoryEntry.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_struct(x0, raritan.rpc.firmware.UpdateHistoryEntry, DecodeException)
            return _ret_

    class _getImageStatus(Interface.Method):
        name = 'getImageStatus'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.firmware.ImageStatus.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.firmware.ImageStatus, DecodeException)
            return _ret_

    class _discardImage(Interface.Method):
        name = 'discardImage'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            return None

    class _getImageInfo(Interface.Method):
        name = 'getImageInfo'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            info = raritan.rpc.firmware.ImageInfo.decode(rsp['info'], agent)
            typecheck.is_bool(_ret_, DecodeException)
            typecheck.is_struct(info, raritan.rpc.firmware.ImageInfo, DecodeException)
            return (_ret_, info)

    class _startUpdate(Interface.Method):
        name = 'startUpdate'

        @staticmethod
        def encode(flags):
            for x0 in flags:
                typecheck.is_enum(x0, raritan.rpc.firmware.UpdateFlags, AssertionError)
            args = {}
            args['flags'] = [raritan.rpc.firmware.UpdateFlags.encode(x0) for x0 in flags]
            return args

        @staticmethod
        def decode(rsp, agent):
            return None
    def __init__(self, target, agent):
        super(Firmware, self).__init__(target, agent)
        self.reboot = Firmware._reboot(self)
        self.factoryReset = Firmware._factoryReset(self)
        self.hardFactoryReset = Firmware._hardFactoryReset(self)
        self.manufacturingReset = Firmware._manufacturingReset(self)
        self.getVersion = Firmware._getVersion(self)
        self.getUpdateHistory = Firmware._getUpdateHistory(self)
        self.getImageStatus = Firmware._getImageStatus(self)
        self.discardImage = Firmware._discardImage(self)
        self.getImageInfo = Firmware._getImageInfo(self)
        self.startUpdate = Firmware._startUpdate(self)

#
# Section generated by IdlC from "FirmwareUpdateStatus.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.firmware


# structure
class UpdateStatus(Structure):
    idlType = "firmware.UpdateStatus:1.0.0"
    elements = ["state", "elapsed", "estimated", "error_message"]

    def __init__(self, state, elapsed, estimated, error_message):
        typecheck.is_string(state, AssertionError)
        typecheck.is_int(elapsed, AssertionError)
        typecheck.is_int(estimated, AssertionError)
        typecheck.is_string(error_message, AssertionError)

        self.state = state
        self.elapsed = elapsed
        self.estimated = estimated
        self.error_message = error_message

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            state = json['state'],
            elapsed = json['elapsed'],
            estimated = json['estimated'],
            error_message = json['error_message'],
        )
        return obj

    def encode(self):
        json = {}
        json['state'] = self.state
        json['elapsed'] = self.elapsed
        json['estimated'] = self.estimated
        json['error_message'] = self.error_message
        return json

# interface
class FirmwareUpdateStatus(Interface):
    idlType = "firmware.FirmwareUpdateStatus:1.0.0"

    class _getStatus(Interface.Method):
        name = 'getStatus'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.firmware.UpdateStatus.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.firmware.UpdateStatus, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(FirmwareUpdateStatus, self).__init__(target, agent)
        self.getStatus = FirmwareUpdateStatus._getStatus(self)

# from raritan/rpc/firmware/__extend__.py
def upload(agent, data, lowMemoryUploadOptions = None):
    """
    Method to upload firmware images

    **parameters**, **return**

    :param agent: An agent instance for the device where the image should be uploaded
    :param data: The binary data of the firmware image
    :param lowMemoryUploadOptions: optional, set options for low memory upload

    **Example**
        :Example:

        from raritan import rpc
        from raritan.rpc import firmware

        agent = rpc.Agent("https", "my-pdu.example.com", "admin", "raritan")
        firmware_proxy = firmware.Firmware("/firmware", agent)

        # read file in binary mode
        fwFile = open("pdu-030600-45660.bin", "rb")
        # upload
        firmware.upload(agent, fwFile.read())

    """

    lowMemoryUploadParams = ""
    if lowMemoryUploadOptions:
        lowMemoryUpload = lowMemoryUploadOptions.get("lowMemoryUpload", "0")
        allowLowMemoryDowngrade = lowMemoryUploadOptions.get("allowLowMemoryDowngrade", "0")
        allowLowMemoryUntrusted = lowMemoryUploadOptions.get("allowLowMemoryUntrusted", "0")

        lowMemoryUploadParams = "?lowMemoryUpload={0}&allowLowMemoryDowngrade={1}&allowLowMemoryUntrusted={2}" \
                                .format(lowMemoryUpload, allowLowMemoryDowngrade, allowLowMemoryUntrusted)

    target = "cgi-bin/fwupload.cgi" + lowMemoryUploadParams
    formdata = [dict(data=data, filename="upfile.bin", formname="upfile", mimetype="application/octet-stream")]
    agent.form_data_file(target, formdata)
