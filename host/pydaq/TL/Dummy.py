#
# ------------------------------------------------------------
# Copyright (c) SILAB , Physics Institute of Bonn University
# ------------------------------------------------------------
#
# SVN revision information:
#  $Rev::                       $:
#  $Author::                    $:
#  $Date::                      $:
#

from TL.TransferLayer import TransferLayer
import array


class Dummy (TransferLayer):

    def __init__(self, conf):
        TransferLayer.__init__(self, conf)

    def init(self):
        print "Init Dummy TransferLayer"
        print "Conf:", str(self._conf)

    def write(self, addr, data):
        #import traceback
        #for line in traceback.format_stack():
        #    print line.strip()

        print "DummyTransferLayer.write addr:", addr, "data:", data

    def read(self, addr, size):
        print "DummyTransferLayer.read addr:", addr, "size:", size
        return array.array('B', '\x00' * size)
