import os
import string


customerService = {
    "key": "CUSTOMER_SERVICE",
    "project": "hackethon-283217"
}

personalAssistant = {
    "key": "PERSONAL_ASSISTANT",
    "project": "online-shopping-spsvwi"
}


def write_to_file(key: string):
    with open(f"{key}.json", 'w') as outfile:
        outfile.write(os.environ[key])


if not os.environ.get("LOCAL") == "true":
    write_to_file(customerService["key"])
    write_to_file(personalAssistant["key"])
