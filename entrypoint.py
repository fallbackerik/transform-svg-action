import sys
import os
import datetime

os.environ["GITHUB_OUTPUT"] = f"time={datetime.datetime.now())}"
print("Hello ", sys.argv[1], "!")
