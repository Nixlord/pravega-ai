import os
import json

if not os.environ["LOCAL"]:
    content = os.environ["GOOGLE_API_CREDENTIALS"]
    with open('credentials.json', 'w') as outfile:
        json.dump(content, outfile)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
