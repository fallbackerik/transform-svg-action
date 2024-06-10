import sys
import os
import datetime

os.environ["GITHUB_OUTPUT"] = f"time={datetime.datetime.now()}"
os.environ["GITHUB_OUTPUT"] += f" svgs-modified=1.svg 2.svg 3.svg"
print("Hello ", str(sys.argv), ":", os.environ["GITHUB_OUTPUT"], "!")
