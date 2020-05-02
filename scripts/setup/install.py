import os
from typing import List

# Took this approach as these are platform independent code, but writing
# in bash/powershell will lock them down

website = os.environ.get("website") or "website"
heroku = os.environ.get("heroku") or "pravegapredictor"

commands = f"""
pip install -r requirements.windows
cd {website} && npm install && cd ..
git remote add heroku git@heroku.com:{heroku}.git
"""


def non_empty(elements: List[str]) -> List[str]:
    return [element for element in elements if len(element) != 0]


command_array = non_empty(commands.split('\n'))

for command in command_array:
    os.system(command)
