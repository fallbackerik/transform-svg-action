import sys
import random
import glob

import xml.etree.ElementTree as etree

with etree.parse(glob.glob(sys.argv[2])) as tree:
  pass
