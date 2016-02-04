#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os

# add custom libraries
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'libs'))
if not path in sys.path:
    print(path)
    sys.path.insert(1, path)
del path

from wb_file_manager import WishboneFileManager

''' this programm controlls the general flow '''

__author__ = "Harald Heckmann"
__copyright__ = "Copyright 2016"
__credits__ = ["Prof. Dr. Steffen Reith", "Harald Heckmann"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Harald Heckmann"
__email__ = "harald.heckmann@student.hs-rm.de"
__status__ = "Development (alpha)"

if __name__ == '__main__':
    myclass = WishboneFileManager()
    myclass.parse()
    myclass.printConfigContent()