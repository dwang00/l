#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/dwang00/")
sys.path.insert(0,"/var/www/dwang00/dwang00/")

import logging
logging.basicConfig(stream=sys.stderr)

from dwang00 import app as application
