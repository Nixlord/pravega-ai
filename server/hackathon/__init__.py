import os
import json

content = os.environ["GOOGLE_API_CREDENTIALS"]


with open('credentials.json', 'w') as outfile:
    json.dump(content, outfile)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
