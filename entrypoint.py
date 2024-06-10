import sys
import random
import glob

import xml.etree.ElementTree as etree

for file in glob.glob(sys.argv[2]):
  print("opening...", file)
  tree = etree.parse(file)
  root = tree.getroot()
