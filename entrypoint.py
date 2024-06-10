import sys
import random
import glob

import xml.etree.ElementTree as etree

for file in glob.glob(sys.argv[2]):
  print("opening...", file)
  with etree.parse(file) as tree:
    pass
