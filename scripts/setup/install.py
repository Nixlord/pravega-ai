import os

# Took this approach as these are platform independent code, but writing
# in bash/powershell will lock them down

commands = """
pip install -r requirements.txt
cd website
npm install 
cd ..
git remote add heroku
"""