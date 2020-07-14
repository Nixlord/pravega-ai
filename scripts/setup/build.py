import os
from typing import List
from distutils.dir_util import copy_tree, remove_tree

source = os.environ.get("source") or "website"
target = os.environ.get("target") or "server/build"

# Replace with python functions

os.system(f"cd {source} && npm run build && cd ..")
copy_tree(src=f"{source}/build", dst=target)
remove_tree(directory=f"{source}/build")

copy_tree(src=f"{target}/static", dst=target)
remove_tree(directory=f"{target}/static")
