# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2020 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "Cfg.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.cfg


# structure
class KeyValue(Structure):
    idlType = "cfg.KeyValue:1.0.0"
    elements = ["key", "value"]

    def __init__(self, key, value):
        typecheck.is_string(key, AssertionError)
        typecheck.is_string(value, AssertionError)

        self.key = key
        self.value = value

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            key = json['key'],
            value = json['value'],
        )
        return obj

    def encode(self):
        json = {}
        json['key'] = self.key
        json['value'] = self.value
        return json

# interface
class Cfg(Interface):
    idlType = "cfg.Cfg:1.0.1"

    ERR_INVALID_KEY = 1

    ERR_INVALID_VALUE = 2

    ERR_NOT_ALLOWED_IN_FIPS_MODE = 3

    class _getValues(Interface.Method):
        name = 'getValues'

        @staticmethod
        def encode(keys):
            for x0 in keys:
                typecheck.is_string(x0, AssertionError)
            args = {}
            args['keys'] = [x0 for x0 in keys]
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            values = [x0 for x0 in rsp['values']]
            typecheck.is_int(_ret_, DecodeException)
            for x0 in values:
                typecheck.is_string(x0, DecodeException)
            return (_ret_, values)

    class _setValues(Interface.Method):
        name = 'setValues'

        @staticmethod
        def encode(keyvaluepairs):
            for x0 in keyvaluepairs:
                typecheck.is_struct(x0, raritan.rpc.cfg.KeyValue, AssertionError)
            args = {}
            args['keyvaluepairs'] = [raritan.rpc.cfg.KeyValue.encode(x0) for x0 in keyvaluepairs]
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(Cfg, self).__init__(target, agent)
        self.getValues = Cfg._getValues(self)
        self.setValues = Cfg._setValues(self)
