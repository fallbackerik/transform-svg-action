import sys
import os
import datetime
import glob

for argv in sys.argv:
  print(argv, glob.glob(sys.argv[2]))

with open(os.environ["GITHUB_OUTPUT"], "a") as output:
  output.write(f"time={datetime.datetime.now()}\n")
  output.write(f"svgs-modified=1.svg 2.svg 3.svg\n")
print("Hello ", str(sys.argv), ":", os.environ["GITHUB_OUTPUT"], "!")
