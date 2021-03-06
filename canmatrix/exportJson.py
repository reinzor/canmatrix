from builtins import *
#!/usr/bin/env python

from .canmatrix import *
import codecs
import json
import sys

#Copyright (c) 2013, Eduard Broecker
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that
# the following conditions are met:
#
#    Redistributions of source code must retain the above copyright notice, this list of conditions and the
#    following disclaimer.
#    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
#DAMAGE.

#
# this script exports json-files from a canmatrix-object
# json-files are the can-matrix-definitions of the CANard-project (https://github.com/ericevenchick/CANard)


def exportJson(db, filename):
    dbfExportEncoding = 'iso-8859-1'

    if (sys.version_info > (3, 0)):
        mode = 'w'
    else:
        mode = 'wb'
    f = open(filename, mode)

    exportArray = []

    for frame in db._fl._list:
        signals = []
        for signal in frame._signals:
            signals.append({
                "name" : signal._name,
                "start_bit" : signal.getLsbStartbit(),
                "bit_length" : signal._signalsize,
                "factor":float(signal._factor),
                "offset":float(signal._offset),
                "is_big_endian":signal._byteorder == 0,
                "is_signed":signal._valuetype == "-"
            })

        exportArray.append({"name" : frame._name, "id" : int(frame._Id), "signals": signals })

    json.dump({"messages" : exportArray}, f, sort_keys=True, indent=4, separators=(',', ': '))
