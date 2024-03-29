# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2010 Raritan Inc. All rights reserved.

from __future__ import absolute_import

import time, calendar
from datetime import datetime

#
# Decodes UNIX timestamp (UTC secs since epoch) to python datetime and vice versa.
#
class Time(datetime):
    def __new__(cls, *x):
        return datetime.__new__(cls, *x)

    @staticmethod
    def decode(json):
        if not isinstance(json, int): raise ValueError
        return Time.utcfromtimestamp(json)

    def encode(self):
        timestamp = calendar.timegm(self.utctimetuple())
        return timestamp

    def __str__(self):
        return self.isoformat(' ') + " (UTC)"
