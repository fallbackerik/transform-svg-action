import sys
import os
import datetime
import glob

print(glob.glob(sys.argv[1]))

with open(os.environ["GITHUB_OUTPUT"], "a") as output:
  output.write(f"time={datetime.datetime.now()}\n")
  output.write(f"svgs-modified=1.svg 2.svg 3.svg\n")
print("Hello ", str(sys.argv), ":", os.environ["GITHUB_OUTPUT"], "!")
