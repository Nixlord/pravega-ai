import os
from typing import List
from distutils.dir_util import copy_tree

source = os.environ.get("source") or "website"
target = os.environ.get("target") or "server/build"

# Took this approach as these are platform independent code, but writing
# in bash/powershell will lock them down
os.system(f"cd {source} && npm run build && cd ..")
copy_tree(src=f"{source}/build", dst=target)

