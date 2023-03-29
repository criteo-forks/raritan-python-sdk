# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2022 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "AnalogModem.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.idl

import raritan.rpc.serial


# interface
class AnalogModem(Interface):
    idlType = "serial.AnalogModem:1.0.0"

    SUCCESS = 0

    ERR_INVALID_VALUE = 1

    # structure
    class Settings(Structure):
        idlType = "serial.AnalogModem.Settings:1.0.0"
        elements = ["dialInEnabled", "ringsUntilAnswer"]

        def __init__(self, dialInEnabled, ringsUntilAnswer):
            typecheck.is_bool(dialInEnabled, AssertionError)
            typecheck.is_int(ringsUntilAnswer, AssertionError)

            self.dialInEnabled = dialInEnabled
            self.ringsUntilAnswer = ringsUntilAnswer

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                dialInEnabled = json['dialInEnabled'],
                ringsUntilAnswer = json['ringsUntilAnswer'],
            )
            return obj

        def encode(self):
            json = {}
            json['dialInEnabled'] = self.dialInEnabled
            json['ringsUntilAnswer'] = self.ringsUntilAnswer
            return json

    # value object
    class DialInEvent(raritan.rpc.idl.Event):
        idlType = "serial.AnalogModem.DialInEvent:1.0.0"

        def __init__(self, number, source):
            super(raritan.rpc.serial.AnalogModem.DialInEvent, self).__init__(source)
            typecheck.is_string(number, AssertionError)

            self.number = number

        def encode(self):
            json = super(raritan.rpc.serial.AnalogModem.DialInEvent, self).encode()
            json['number'] = self.number
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                number = json['number'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["number"]
            elements = elements + super(raritan.rpc.serial.AnalogModem.DialInEvent, self).listElements()
            return elements

    # value object
    class CallReceivedEvent(DialInEvent):
        idlType = "serial.AnalogModem.CallReceivedEvent:1.0.0"

        def __init__(self, number, source):
            super(raritan.rpc.serial.AnalogModem.CallReceivedEvent, self).__init__(number, source)

        def encode(self):
            json = super(raritan.rpc.serial.AnalogModem.CallReceivedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for serial.AnalogModem.DialInEvent
                number = json['number'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.serial.AnalogModem.CallReceivedEvent, self).listElements()
            return elements

    # value object
    class CallEndedEvent(DialInEvent):
        idlType = "serial.AnalogModem.CallEndedEvent:1.0.0"

        def __init__(self, disconnectedRemotely, number, source):
            super(raritan.rpc.serial.AnalogModem.CallEndedEvent, self).__init__(number, source)
            typecheck.is_bool(disconnectedRemotely, AssertionError)

            self.disconnectedRemotely = disconnectedRemotely

        def encode(self):
            json = super(raritan.rpc.serial.AnalogModem.CallEndedEvent, self).encode()
            json['disconnectedRemotely'] = self.disconnectedRemotely
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                disconnectedRemotely = json['disconnectedRemotely'],
                # for serial.AnalogModem.DialInEvent
                number = json['number'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["disconnectedRemotely"]
            elements = elements + super(raritan.rpc.serial.AnalogModem.CallEndedEvent, self).listElements()
            return elements

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.serial.AnalogModem.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.serial.AnalogModem.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.serial.AnalogModem.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.serial.AnalogModem.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(AnalogModem, self).__init__(target, agent)
        self.getSettings = AnalogModem._getSettings(self)
        self.setSettings = AnalogModem._setSettings(self)

#
# Section generated by IdlC from "GsmModem.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.idl

import raritan.rpc.serial


# interface
class GsmModem(Interface):
    idlType = "serial.GsmModem:1.0.2"

    SUCCESS = 0

    ERR_INVALID_VALUE = 1

    ERR_WRONG_PIN = 2

    ERR_SMS_SEND_FAILED = 3

    ERR_COMMUNICATION_FAILURE = 4

    ERR_SIM_LOCKED = 5

    ERR_WRONG_SIM_STATUS = 6

    ERR_WRONG_PUK = 7

    ERR_SIM_PROBLEM = 8

    # enumeration
    class SimSecurityStatus(Enumeration):
        idlType = "serial.GsmModem_1_0_2.SimSecurityStatus:1.0.0"
        values = ["UNLOCKED", "WAITFORPIN", "WAITFORPUK", "UNKNOWN"]

    SimSecurityStatus.UNLOCKED = SimSecurityStatus(0)
    SimSecurityStatus.WAITFORPIN = SimSecurityStatus(1)
    SimSecurityStatus.WAITFORPUK = SimSecurityStatus(2)
    SimSecurityStatus.UNKNOWN = SimSecurityStatus(3)

    # structure
    class Settings(Structure):
        idlType = "serial.GsmModem_1_0_2.Settings:1.0.0"
        elements = ["pin", "smsc"]

        def __init__(self, pin, smsc):
            typecheck.is_string(pin, AssertionError)
            typecheck.is_string(smsc, AssertionError)

            self.pin = pin
            self.smsc = smsc

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                pin = json['pin'],
                smsc = json['smsc'],
            )
            return obj

        def encode(self):
            json = {}
            json['pin'] = self.pin
            json['smsc'] = self.smsc
            return json

    # structure
    class Information(Structure):
        idlType = "serial.GsmModem_1_0_2.Information:1.0.0"
        elements = ["imei", "imsi", "manufacturer", "model", "revision", "ownNumber", "simSmsc", "networkName", "serviceProviderName", "receptionLevel"]

        def __init__(self, imei, imsi, manufacturer, model, revision, ownNumber, simSmsc, networkName, serviceProviderName, receptionLevel):
            typecheck.is_string(imei, AssertionError)
            typecheck.is_string(imsi, AssertionError)
            typecheck.is_string(manufacturer, AssertionError)
            typecheck.is_string(model, AssertionError)
            typecheck.is_string(revision, AssertionError)
            typecheck.is_string(ownNumber, AssertionError)
            typecheck.is_string(simSmsc, AssertionError)
            typecheck.is_string(networkName, AssertionError)
            typecheck.is_string(serviceProviderName, AssertionError)
            typecheck.is_int(receptionLevel, AssertionError)

            self.imei = imei
            self.imsi = imsi
            self.manufacturer = manufacturer
            self.model = model
            self.revision = revision
            self.ownNumber = ownNumber
            self.simSmsc = simSmsc
            self.networkName = networkName
            self.serviceProviderName = serviceProviderName
            self.receptionLevel = receptionLevel

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                imei = json['imei'],
                imsi = json['imsi'],
                manufacturer = json['manufacturer'],
                model = json['model'],
                revision = json['revision'],
                ownNumber = json['ownNumber'],
                simSmsc = json['simSmsc'],
                networkName = json['networkName'],
                serviceProviderName = json['serviceProviderName'],
                receptionLevel = json['receptionLevel'],
            )
            return obj

        def encode(self):
            json = {}
            json['imei'] = self.imei
            json['imsi'] = self.imsi
            json['manufacturer'] = self.manufacturer
            json['model'] = self.model
            json['revision'] = self.revision
            json['ownNumber'] = self.ownNumber
            json['simSmsc'] = self.simSmsc
            json['networkName'] = self.networkName
            json['serviceProviderName'] = self.serviceProviderName
            json['receptionLevel'] = self.receptionLevel
            return json

    # value object
    class SimSecurityStatusChangedEvent(raritan.rpc.idl.Event):
        idlType = "serial.GsmModem_1_0_2.SimSecurityStatusChangedEvent:1.0.0"

        def __init__(self, newSimStatus, source):
            super(raritan.rpc.serial.GsmModem.SimSecurityStatusChangedEvent, self).__init__(source)
            typecheck.is_enum(newSimStatus, raritan.rpc.serial.GsmModem.SimSecurityStatus, AssertionError)

            self.newSimStatus = newSimStatus

        def encode(self):
            json = super(raritan.rpc.serial.GsmModem.SimSecurityStatusChangedEvent, self).encode()
            json['newSimStatus'] = raritan.rpc.serial.GsmModem.SimSecurityStatus.encode(self.newSimStatus)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                newSimStatus = raritan.rpc.serial.GsmModem.SimSecurityStatus.decode(json['newSimStatus']),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["newSimStatus"]
            elements = elements + super(raritan.rpc.serial.GsmModem.SimSecurityStatusChangedEvent, self).listElements()
            return elements

    # value object
    class SimPinUpdatedEvent(raritan.rpc.idl.Event):
        idlType = "serial.GsmModem_1_0_2.SimPinUpdatedEvent:1.0.0"

        def __init__(self, newPin, source):
            super(raritan.rpc.serial.GsmModem.SimPinUpdatedEvent, self).__init__(source)
            typecheck.is_string(newPin, AssertionError)

            self.newPin = newPin

        def encode(self):
            json = super(raritan.rpc.serial.GsmModem.SimPinUpdatedEvent, self).encode()
            json['newPin'] = self.newPin
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                newPin = json['newPin'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["newPin"]
            elements = elements + super(raritan.rpc.serial.GsmModem.SimPinUpdatedEvent, self).listElements()
            return elements

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.serial.GsmModem.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.serial.GsmModem.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.serial.GsmModem.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.serial.GsmModem.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _sendSms(Interface.Method):
        name = 'sendSms'

        @staticmethod
        def encode(recipient, text):
            typecheck.is_string(recipient, AssertionError)
            typecheck.is_string(text, AssertionError)
            args = {}
            args['recipient'] = recipient
            args['text'] = text
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _sendTestSms(Interface.Method):
        name = 'sendTestSms'

        @staticmethod
        def encode(recipient, testSettings):
            typecheck.is_string(recipient, AssertionError)
            typecheck.is_struct(testSettings, raritan.rpc.serial.GsmModem.Settings, AssertionError)
            args = {}
            args['recipient'] = recipient
            args['testSettings'] = raritan.rpc.serial.GsmModem.Settings.encode(testSettings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getInformation(Interface.Method):
        name = 'getInformation'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            info = raritan.rpc.serial.GsmModem.Information.decode(rsp['info'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(info, raritan.rpc.serial.GsmModem.Information, DecodeException)
            return (_ret_, info)

    class _getInformationWithPin(Interface.Method):
        name = 'getInformationWithPin'

        @staticmethod
        def encode(pin):
            typecheck.is_string(pin, AssertionError)
            args = {}
            args['pin'] = pin
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            info = raritan.rpc.serial.GsmModem.Information.decode(rsp['info'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(info, raritan.rpc.serial.GsmModem.Information, DecodeException)
            return (_ret_, info)

    class _getSimSecurityStatus(Interface.Method):
        name = 'getSimSecurityStatus'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            simStatus = raritan.rpc.serial.GsmModem.SimSecurityStatus.decode(rsp['simStatus'])
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_enum(simStatus, raritan.rpc.serial.GsmModem.SimSecurityStatus, DecodeException)
            return (_ret_, simStatus)

    class _unlockSimCard(Interface.Method):
        name = 'unlockSimCard'

        @staticmethod
        def encode(puk, newPin):
            typecheck.is_string(puk, AssertionError)
            typecheck.is_string(newPin, AssertionError)
            args = {}
            args['puk'] = puk
            args['newPin'] = newPin
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(GsmModem, self).__init__(target, agent)
        self.getSettings = GsmModem._getSettings(self)
        self.setSettings = GsmModem._setSettings(self)
        self.sendSms = GsmModem._sendSms(self)
        self.sendTestSms = GsmModem._sendTestSms(self)
        self.getInformation = GsmModem._getInformation(self)
        self.getInformationWithPin = GsmModem._getInformationWithPin(self)
        self.getSimSecurityStatus = GsmModem._getSimSecurityStatus(self)
        self.unlockSimCard = GsmModem._unlockSimCard(self)

#
# Section generated by IdlC from "SerialPort.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.idl

import raritan.rpc.serial


# interface
class SerialPort(Interface):
    idlType = "serial.SerialPort:3.0.1"

    SUCCESS = 0

    ERR_INVALID_VALUE = 1

    # enumeration
    class PortState(Enumeration):
        idlType = "serial.SerialPort_3_0_1.PortState:1.0.0"
        values = ["CONSOLE", "ANALOGMODEM", "GSMMODEM", "DISCONNECTED"]

    PortState.CONSOLE = PortState(0)
    PortState.ANALOGMODEM = PortState(1)
    PortState.GSMMODEM = PortState(2)
    PortState.DISCONNECTED = PortState(3)

    # enumeration
    class DetectionType(Enumeration):
        idlType = "serial.SerialPort_3_0_1.DetectionType:1.0.0"
        values = ["AUTOMATIC", "FORCE_CONSOLE", "FORCE_ANALOGMODEM", "FORCE_GSMMODEM"]

    DetectionType.AUTOMATIC = DetectionType(0)
    DetectionType.FORCE_CONSOLE = DetectionType(1)
    DetectionType.FORCE_ANALOGMODEM = DetectionType(2)
    DetectionType.FORCE_GSMMODEM = DetectionType(3)

    # enumeration
    class BaudRate(Enumeration):
        idlType = "serial.SerialPort_3_0_1.BaudRate:1.0.0"
        values = ["BR1200", "BR2400", "BR4800", "BR9600", "BR19200", "BR38400", "BR57600", "BR115200"]

    BaudRate.BR1200 = BaudRate(0)
    BaudRate.BR2400 = BaudRate(1)
    BaudRate.BR4800 = BaudRate(2)
    BaudRate.BR9600 = BaudRate(3)
    BaudRate.BR19200 = BaudRate(4)
    BaudRate.BR38400 = BaudRate(5)
    BaudRate.BR57600 = BaudRate(6)
    BaudRate.BR115200 = BaudRate(7)

    # structure
    class MetaData(Structure):
        idlType = "serial.SerialPort_3_0_1.MetaData:1.0.0"
        elements = ["hasModemSupport"]

        def __init__(self, hasModemSupport):
            typecheck.is_bool(hasModemSupport, AssertionError)

            self.hasModemSupport = hasModemSupport

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                hasModemSupport = json['hasModemSupport'],
            )
            return obj

        def encode(self):
            json = {}
            json['hasModemSupport'] = self.hasModemSupport
            return json

    # structure
    class State(Structure):
        idlType = "serial.SerialPort_3_0_1.State:1.0.0"
        elements = ["state", "deviceName"]

        def __init__(self, state, deviceName):
            typecheck.is_enum(state, raritan.rpc.serial.SerialPort.PortState, AssertionError)
            typecheck.is_string(deviceName, AssertionError)

            self.state = state
            self.deviceName = deviceName

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                state = raritan.rpc.serial.SerialPort.PortState.decode(json['state']),
                deviceName = json['deviceName'],
            )
            return obj

        def encode(self):
            json = {}
            json['state'] = raritan.rpc.serial.SerialPort.PortState.encode(self.state)
            json['deviceName'] = self.deviceName
            return json

    # structure
    class Settings(Structure):
        idlType = "serial.SerialPort_3_0_1.Settings:1.0.0"
        elements = ["consoleBaudRate", "modemBaudRate", "detectType"]

        def __init__(self, consoleBaudRate, modemBaudRate, detectType):
            typecheck.is_enum(consoleBaudRate, raritan.rpc.serial.SerialPort.BaudRate, AssertionError)
            typecheck.is_enum(modemBaudRate, raritan.rpc.serial.SerialPort.BaudRate, AssertionError)
            typecheck.is_enum(detectType, raritan.rpc.serial.SerialPort.DetectionType, AssertionError)

            self.consoleBaudRate = consoleBaudRate
            self.modemBaudRate = modemBaudRate
            self.detectType = detectType

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                consoleBaudRate = raritan.rpc.serial.SerialPort.BaudRate.decode(json['consoleBaudRate']),
                modemBaudRate = raritan.rpc.serial.SerialPort.BaudRate.decode(json['modemBaudRate']),
                detectType = raritan.rpc.serial.SerialPort.DetectionType.decode(json['detectType']),
            )
            return obj

        def encode(self):
            json = {}
            json['consoleBaudRate'] = raritan.rpc.serial.SerialPort.BaudRate.encode(self.consoleBaudRate)
            json['modemBaudRate'] = raritan.rpc.serial.SerialPort.BaudRate.encode(self.modemBaudRate)
            json['detectType'] = raritan.rpc.serial.SerialPort.DetectionType.encode(self.detectType)
            return json

    # value object
    class ModemEvent(raritan.rpc.idl.Event):
        idlType = "serial.SerialPort_3_0_1.ModemEvent:1.0.0"

        def __init__(self, modem, source):
            super(raritan.rpc.serial.SerialPort.ModemEvent, self).__init__(source)
            typecheck.is_remote_obj(modem, AssertionError)

            self.modem = modem

        def encode(self):
            json = super(raritan.rpc.serial.SerialPort.ModemEvent, self).encode()
            json['modem'] = Interface.encode(self.modem)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                modem = Interface.decode(json['modem'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["modem"]
            elements = elements + super(raritan.rpc.serial.SerialPort.ModemEvent, self).listElements()
            return elements

    # value object
    class ModemAddedEvent(ModemEvent):
        idlType = "serial.SerialPort_3_0_1.ModemAddedEvent:1.0.0"

        def __init__(self, modem, source):
            super(raritan.rpc.serial.SerialPort.ModemAddedEvent, self).__init__(modem, source)

        def encode(self):
            json = super(raritan.rpc.serial.SerialPort.ModemAddedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for serial.SerialPort_3_0_1.ModemEvent
                modem = Interface.decode(json['modem'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.serial.SerialPort.ModemAddedEvent, self).listElements()
            return elements

    # value object
    class ModemRemovedEvent(ModemEvent):
        idlType = "serial.SerialPort_3_0_1.ModemRemovedEvent:1.0.0"

        def __init__(self, modem, source):
            super(raritan.rpc.serial.SerialPort.ModemRemovedEvent, self).__init__(modem, source)

        def encode(self):
            json = super(raritan.rpc.serial.SerialPort.ModemRemovedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for serial.SerialPort_3_0_1.ModemEvent
                modem = Interface.decode(json['modem'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.serial.SerialPort.ModemRemovedEvent, self).listElements()
            return elements

    class _getMetaData(Interface.Method):
        name = 'getMetaData'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.serial.SerialPort.MetaData.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.serial.SerialPort.MetaData, DecodeException)
            return _ret_

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.serial.SerialPort.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.serial.SerialPort.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.serial.SerialPort.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.serial.SerialPort.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getState(Interface.Method):
        name = 'getState'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.serial.SerialPort.State.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.serial.SerialPort.State, DecodeException)
            return _ret_

    class _getModem(Interface.Method):
        name = 'getModem'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = Interface.decode(rsp['_ret_'], agent)
            typecheck.is_remote_obj(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(SerialPort, self).__init__(target, agent)
        self.getMetaData = SerialPort._getMetaData(self)
        self.getSettings = SerialPort._getSettings(self)
        self.setSettings = SerialPort._setSettings(self)
        self.getState = SerialPort._getState(self)
        self.getModem = SerialPort._getModem(self)

#
# Section generated by IdlC from "PortDispatcher.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# interface
class PortDispatcher(Interface):
    idlType = "serial.PortDispatcher:1.2.2"

    class _getPorts(Interface.Method):
        name = 'getPorts'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = dict([(
                elem['key'],
                Interface.decode(elem['value'], agent))
                for elem in rsp['_ret_']])
            return _ret_
    def __init__(self, target, agent):
        super(PortDispatcher, self).__init__(target, agent)
        self.getPorts = PortDispatcher._getPorts(self)
