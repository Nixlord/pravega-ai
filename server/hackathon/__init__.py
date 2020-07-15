import os
import json

if os.environ.get("LOCAL") == "true":
    content = os.environ["GOOGLE_API_CREDENTIALS"]
    with open('credentials.json', 'w') as outfile:
        json.dump(content, outfile)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
