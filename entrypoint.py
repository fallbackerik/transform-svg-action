import sys
import os
import random
import glob

import xml.etree.ElementTree as etree

SVG_NAMESPACE = "https://www.w3.org/2000/svg"
modified = []
for file in glob.glob(sys.argv[2]):
  filebase = os.path.basename(file)
  print("opening...", filebase)
  tree = etree.parse(file)
  root = tree.getroot()

  if not "svg" in root.attrib.get("xmlns", "attrib xmlns doesn't exist"):
    root.attrib["xmlns"] = SVG_NAMESPACE
    tree = etree.ElementTree(root)

  if "width" not in root.attrib or "height" not in root.attrib:
    raise ValueError("Expected the svg root element to contain width and height attributes.")

  width = int(root.attrib["width"])
  height = int(root.attrib["height"])

  radius = random.randint(3, 30)
  cx_gen = random.randint(5, 95)
  cy_gen = random.randint(5, 95)

  # limit at picture boundaries
  cx_gen_wl = max(cx_gen , radius+1)
  cx_gen_wlwr = min(cx_gen_wl, 99-radius)
  cy_gen_wl = max(cy_gen, radius+1)
  cy_gen_wlwr = min(cy_gen_wl, 99-radius)
  
  circle = etree.Element("circle", {
    "cx" : f"{cx_gen_wlwr}%",
    "cy" : f"{cy_gen_wlwr}%",
    "r" : f"{radius}%",
    "fill" : "red",
  })
  root.append(circle)
  tree.write(f"output/{filebase}", xml_declaration=True, encoding="utf-8")
  modified.append(filebase)

with open(os.environ["GITHUB_OUTPUT"], "a") as output:
  output.write(f"svgs-modified={" ".join(modified)}\n")
