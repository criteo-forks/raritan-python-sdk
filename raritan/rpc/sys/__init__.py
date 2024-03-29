# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2022 Raritan Inc. All rights reserved.
#
# This is an auto-generated file.

#
# Section generated by IdlC from "System.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# interface
class System(Interface):
    idlType = "sys.System:1.0.0"

    class _isDaemonRunning(Interface.Method):
        name = 'isDaemonRunning'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_bool(_ret_, DecodeException)
            return _ret_

    class _restartDaemon(Interface.Method):
        name = 'restartDaemon'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            return None
    def __init__(self, target, agent):
        super(System, self).__init__(target, agent)
        self.isDaemonRunning = System._isDaemonRunning(self)
        self.restartDaemon = System._restartDaemon(self)
