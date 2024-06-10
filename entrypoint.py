import sys
import random
import glob

import xml.etree.ElementTree as etree

SVG_NAMESPACE = "https://www.w3.org/2000/svg"

for file in glob.glob(sys.argv[2]):
  print("opening...", file)
  tree = etree.parse(file)
  root = tree.getroot()

  if not "svg" in root.attrib.get("xmlns", "attrib xmlns doesn't exist"):
    root.attrib["xmlns"] = SVG_NAMESPACE
    tree = etree.ElementTree(root)

  if "width" not in root.attrib or "height" not in root.attrib:
    raise ValueError("Expected the svg root element to contain width and height attributes.")
  print("attrib", root.attrib)
