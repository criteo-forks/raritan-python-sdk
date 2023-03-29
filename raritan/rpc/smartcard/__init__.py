# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2022 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "CardReader.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.idl

import raritan.rpc.smartcard


# interface
class CardReader(Interface):
    idlType = "smartcard.CardReader:1.0.4"

    NO_ERROR = 0

    ERR_SLOT_EMPTY = 1

    # structure
    class MetaData(Structure):
        idlType = "smartcard.CardReader_1_0_4.MetaData:1.0.0"
        elements = ["id", "manufacturer", "product", "serialNumber", "channel", "position"]

        def __init__(self, id, manufacturer, product, serialNumber, channel, position):
            typecheck.is_string(id, AssertionError)
            typecheck.is_string(manufacturer, AssertionError)
            typecheck.is_string(product, AssertionError)
            typecheck.is_string(serialNumber, AssertionError)
            typecheck.is_int(channel, AssertionError)
            typecheck.is_string(position, AssertionError)

            self.id = id
            self.manufacturer = manufacturer
            self.product = product
            self.serialNumber = serialNumber
            self.channel = channel
            self.position = position

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                id = json['id'],
                manufacturer = json['manufacturer'],
                product = json['product'],
                serialNumber = json['serialNumber'],
                channel = json['channel'],
                position = json['position'],
            )
            return obj

        def encode(self):
            json = {}
            json['id'] = self.id
            json['manufacturer'] = self.manufacturer
            json['product'] = self.product
            json['serialNumber'] = self.serialNumber
            json['channel'] = self.channel
            json['position'] = self.position
            return json

    # structure
    class CardInformation(Structure):
        idlType = "smartcard.CardReader_1_0_4.CardInformation:1.0.0"
        elements = ["type", "uid"]

        def __init__(self, type, uid):
            typecheck.is_string(type, AssertionError)
            typecheck.is_string(uid, AssertionError)

            self.type = type
            self.uid = uid

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                type = json['type'],
                uid = json['uid'],
            )
            return obj

        def encode(self):
            json = {}
            json['type'] = self.type
            json['uid'] = self.uid
            return json

    # value object
    class CardEvent(raritan.rpc.idl.Event):
        idlType = "smartcard.CardReader_1_0_4.CardEvent:2.0.0"

        def __init__(self, metaData, source):
            super(raritan.rpc.smartcard.CardReader.CardEvent, self).__init__(source)
            typecheck.is_struct(metaData, raritan.rpc.smartcard.CardReader.MetaData, AssertionError)

            self.metaData = metaData

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReader.CardEvent, self).encode()
            json['metaData'] = raritan.rpc.smartcard.CardReader.MetaData.encode(self.metaData)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["metaData"]
            elements = elements + super(raritan.rpc.smartcard.CardReader.CardEvent, self).listElements()
            return elements

    # value object
    class CardInsertedEvent(CardEvent):
        idlType = "smartcard.CardReader_1_0_4.CardInsertedEvent:2.0.0"

        def __init__(self, metaData, source):
            super(raritan.rpc.smartcard.CardReader.CardInsertedEvent, self).__init__(metaData, source)

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReader.CardInsertedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for smartcard.CardReader_1_0_4.CardEvent_2_0_0
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.smartcard.CardReader.CardInsertedEvent, self).listElements()
            return elements

    # value object
    class CardRemovedEvent(CardEvent):
        idlType = "smartcard.CardReader_1_0_4.CardRemovedEvent:2.0.0"

        def __init__(self, metaData, source):
            super(raritan.rpc.smartcard.CardReader.CardRemovedEvent, self).__init__(metaData, source)

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReader.CardRemovedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for smartcard.CardReader_1_0_4.CardEvent_2_0_0
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.smartcard.CardReader.CardRemovedEvent, self).listElements()
            return elements

    class _getMetaData(Interface.Method):
        name = 'getMetaData'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.smartcard.CardReader.MetaData.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.smartcard.CardReader.MetaData, DecodeException)
            return _ret_

    class _getCardInformation(Interface.Method):
        name = 'getCardInformation'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            cardInfo = raritan.rpc.smartcard.CardReader.CardInformation.decode(rsp['cardInfo'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(cardInfo, raritan.rpc.smartcard.CardReader.CardInformation, DecodeException)
            return (_ret_, cardInfo)
    def __init__(self, target, agent):
        super(CardReader, self).__init__(target, agent)
        self.getMetaData = CardReader._getMetaData(self)
        self.getCardInformation = CardReader._getCardInformation(self)

#
# Section generated by IdlC from "CardReaderManager.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.idl

import raritan.rpc.smartcard


# interface
class CardReaderManager(Interface):
    idlType = "smartcard.CardReaderManager:1.0.5"

    # structure
    class CardReaderSettings(Structure):
        idlType = "smartcard.CardReaderManager_1_0_5.CardReaderSettings:1.0.0"
        elements = ["name", "description", "cardFormat"]

        def __init__(self, name, description, cardFormat):
            typecheck.is_string(name, AssertionError)
            typecheck.is_string(description, AssertionError)
            typecheck.is_string(cardFormat, AssertionError)

            self.name = name
            self.description = description
            self.cardFormat = cardFormat

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                name = json['name'],
                description = json['description'],
                cardFormat = json['cardFormat'],
            )
            return obj

        def encode(self):
            json = {}
            json['name'] = self.name
            json['description'] = self.description
            json['cardFormat'] = self.cardFormat
            return json

    # value object
    class CardReaderEvent(raritan.rpc.idl.Event):
        idlType = "smartcard.CardReaderManager_1_0_5.CardReaderEvent:1.0.0"

        def __init__(self, cardReader, metaData, source):
            super(raritan.rpc.smartcard.CardReaderManager.CardReaderEvent, self).__init__(source)
            typecheck.is_interface(cardReader, raritan.rpc.smartcard.CardReader, AssertionError)
            typecheck.is_struct(metaData, raritan.rpc.smartcard.CardReader.MetaData, AssertionError)

            self.cardReader = cardReader
            self.metaData = metaData

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReaderManager.CardReaderEvent, self).encode()
            json['cardReader'] = Interface.encode(self.cardReader)
            json['metaData'] = raritan.rpc.smartcard.CardReader.MetaData.encode(self.metaData)
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                cardReader = Interface.decode(json['cardReader'], agent),
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["cardReader", "metaData"]
            elements = elements + super(raritan.rpc.smartcard.CardReaderManager.CardReaderEvent, self).listElements()
            return elements

    # value object
    class CardReaderAttachedEvent(CardReaderEvent):
        idlType = "smartcard.CardReaderManager_1_0_5.CardReaderAttachedEvent:1.0.0"

        def __init__(self, cardReader, metaData, source):
            super(raritan.rpc.smartcard.CardReaderManager.CardReaderAttachedEvent, self).__init__(cardReader, metaData, source)

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReaderManager.CardReaderAttachedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for smartcard.CardReaderManager_1_0_5.CardReaderEvent
                cardReader = Interface.decode(json['cardReader'], agent),
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.smartcard.CardReaderManager.CardReaderAttachedEvent, self).listElements()
            return elements

    # value object
    class CardReaderDetachedEvent(CardReaderEvent):
        idlType = "smartcard.CardReaderManager_1_0_5.CardReaderDetachedEvent:1.0.0"

        def __init__(self, cardReader, metaData, source):
            super(raritan.rpc.smartcard.CardReaderManager.CardReaderDetachedEvent, self).__init__(cardReader, metaData, source)

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReaderManager.CardReaderDetachedEvent, self).encode()
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                # for smartcard.CardReaderManager_1_0_5.CardReaderEvent
                cardReader = Interface.decode(json['cardReader'], agent),
                metaData = raritan.rpc.smartcard.CardReader.MetaData.decode(json['metaData'], agent),
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = []
            elements = elements + super(raritan.rpc.smartcard.CardReaderManager.CardReaderDetachedEvent, self).listElements()
            return elements

    # value object
    class CardReaderSettingsChangedEvent(raritan.rpc.event.UserEvent):
        idlType = "smartcard.CardReaderManager_1_0_5.CardReaderSettingsChangedEvent:1.0.0"

        def __init__(self, cardReader, oldSettings, newSettings, position, actUserName, actIpAddr, source):
            super(raritan.rpc.smartcard.CardReaderManager.CardReaderSettingsChangedEvent, self).__init__(actUserName, actIpAddr, source)
            typecheck.is_interface(cardReader, raritan.rpc.smartcard.CardReader, AssertionError)
            typecheck.is_struct(oldSettings, raritan.rpc.smartcard.CardReaderManager.CardReaderSettings, AssertionError)
            typecheck.is_struct(newSettings, raritan.rpc.smartcard.CardReaderManager.CardReaderSettings, AssertionError)
            typecheck.is_string(position, AssertionError)

            self.cardReader = cardReader
            self.oldSettings = oldSettings
            self.newSettings = newSettings
            self.position = position

        def encode(self):
            json = super(raritan.rpc.smartcard.CardReaderManager.CardReaderSettingsChangedEvent, self).encode()
            json['cardReader'] = Interface.encode(self.cardReader)
            json['oldSettings'] = raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.encode(self.oldSettings)
            json['newSettings'] = raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.encode(self.newSettings)
            json['position'] = self.position
            return json

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                cardReader = Interface.decode(json['cardReader'], agent),
                oldSettings = raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.decode(json['oldSettings'], agent),
                newSettings = raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.decode(json['newSettings'], agent),
                position = json['position'],
                # for event.UserEvent
                actUserName = json['actUserName'],
                actIpAddr = json['actIpAddr'],
                # for idl.Event
                source = Interface.decode(json['source'], agent),
            )
            return obj

        def listElements(self):
            elements = ["cardReader", "oldSettings", "newSettings", "position"]
            elements = elements + super(raritan.rpc.smartcard.CardReaderManager.CardReaderSettingsChangedEvent, self).listElements()
            return elements

    class _getCardReaders(Interface.Method):
        name = 'getCardReaders'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [Interface.decode(x0, agent) for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_interface(x0, raritan.rpc.smartcard.CardReader, DecodeException)
            return _ret_

    class _getCardReaderById(Interface.Method):
        name = 'getCardReaderById'

        @staticmethod
        def encode(readerId):
            typecheck.is_string(readerId, AssertionError)
            args = {}
            args['readerId'] = readerId
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = Interface.decode(rsp['_ret_'], agent)
            typecheck.is_interface(_ret_, raritan.rpc.smartcard.CardReader, DecodeException)
            return _ret_

    class _setCardReaderSettings(Interface.Method):
        name = 'setCardReaderSettings'

        @staticmethod
        def encode(position, setting):
            typecheck.is_string(position, AssertionError)
            typecheck.is_struct(setting, raritan.rpc.smartcard.CardReaderManager.CardReaderSettings, AssertionError)
            args = {}
            args['position'] = position
            args['setting'] = raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.encode(setting)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getAllCardReaderSettings(Interface.Method):
        name = 'getAllCardReaderSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = dict([(
                elem['key'],
                raritan.rpc.smartcard.CardReaderManager.CardReaderSettings.decode(elem['value'], agent))
                for elem in rsp['_ret_']])
            return _ret_

    class _getSupportedCardFormats(Interface.Method):
        name = 'getSupportedCardFormats'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [x0 for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_string(x0, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(CardReaderManager, self).__init__(target, agent)
        self.getCardReaders = CardReaderManager._getCardReaders(self)
        self.getCardReaderById = CardReaderManager._getCardReaderById(self)
        self.setCardReaderSettings = CardReaderManager._setCardReaderSettings(self)
        self.getAllCardReaderSettings = CardReaderManager._getAllCardReaderSettings(self)
        self.getSupportedCardFormats = CardReaderManager._getSupportedCardFormats(self)
