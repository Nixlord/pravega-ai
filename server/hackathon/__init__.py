import os
import json

if not os.environ.get("LOCAL") == "true":
    content = os.environ["GOOGLE_API_CREDENTIALS"]
    with open('credentials.json', 'w') as outfile:
        outfile.write(content)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
